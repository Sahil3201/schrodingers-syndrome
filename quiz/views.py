from django.contrib.auth.views import LoginView, LogoutView
from random import randint
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Student, Qna, Answers
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

@login_required
def quiz_page(request):
    if request.method == "POST":
        qid = int(request.POST.get("qid"))
        ans = str(request.POST.get("answer"))
        qna = Qna.objects.get(qid=qid)
        correct_answer = qna.answer

        answer = Answers.objects.get(student=request.user, qna=qna)
        if ans.lower().replace(' ','') == correct_answer.lower().replace(' ','') and datetime.timestamp(datetime.now())-answer.shown_at<140:
            answer.correct = True
            stud = Student.objects.get(id=request.user.id)
            stud.score = stud.score + \
                {"E": 10, "M": 20, "H": 30}[qna.difficulty]
            stud.save(update_fields=["score"])
        else:
            answer.correct = False
        answer.save()
        return HttpResponseRedirect(reverse("quiz:quiz"))
    else:
        try:
            ques_answered = Answers.objects.filter(student=request.user)
            answered_qid = []
            for que in ques_answered:
                answered_qid.append(str(que))

            current_que_no = ques_answered.count() + 1
            last_que_difficulty = ques_answered.latest("id").qna.difficulty
            last_que_is_correct = ques_answered.latest("id").correct

            if last_que_is_correct:
                current_diff = "M" if last_que_difficulty == "E" else "H"
            else:
                current_diff = "M" if last_que_difficulty == "H" else "E"

        except:
            answered_qid = []
            current_que_no = 1
            current_diff = "M"
            last_que_difficulty = "M"

        if current_que_no == 21:
            thankyou_context = {'score': request.user.score}
            return render(request, "quiz/thankyou.html", context=thankyou_context)

        grp = 'S' if str(request.user.username)[0]=='1' else 'C'
        qna = get_question(answered_qid, current_diff, grp)
        answer = Answers(student=request.user, qna=qna,
                         shown_at=datetime.timestamp(datetime.now()))
        answer.save()

        context = {"current_que_no": current_que_no,
                   "que_statement": qna.question, "qid": qna.qid}
        return render(request, "quiz/quiz.html", context=context)


def get_question(answered_qid, current_diff, group):
    grp_code = 1 if group == 'S' else 2
    diff_code = 1 if current_diff == "E" else (2 if current_diff == "M" else 3)
    max_count = 25
    while max_count > 0:
        que_no = randint(1, 15)
        que_id = grp_code*10000 + diff_code*1000 + que_no

        if str(que_id) not in answered_qid:
            break
        max_count = max_count - 1
    else:
        if diff_code=='E':
            diff_code = 'M'
        elif diff_code=='M':
            diff_code = 'H'
        else:
            diff_code = 'E'
        get_question(answered_qid,diff_code,group)
    return Qna.objects.get(qid=que_id)

# def get_time_for_question(request):
#     user = request.user
#     ans = Answers.objects.filter(student=user).latest("shown_at").shown_at
#     submit_time_in_sec = (
#         (((ans.hour * 60) + ans.minute) * 60) + ans.second) + 124
#     return HttpResponse(submit_time_in_sec)


class instructions(LoginRequiredMixin, generic.TemplateView):
    template_name = "quiz/instructions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class login(LoginView):
    template_name = "quiz/login.html"
    redirect_authenticated_user = True
    extra_context = {next: 'quiz/'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = '/instuctions'
        return context


class logout(LogoutView):
    template_name = "quiz/logout.html"
    def get(self,request):
        return HttpResponseRedirect(reverse('quiz:login'))
