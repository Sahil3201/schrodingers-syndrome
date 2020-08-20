// // // var countDownDate = new Date("Aug 14, 2020 00:00:01").getTime();
// // // console.log(countDownDate)
// // // Update the count down every 1 second
// // $(document).ready(function () {
// //   // var submit_at = 120;
// //   var distance = 120;

// //   // $.ajax({
// //   //   type: "GET",
// //   //   url: "http://127.0.0.1:8000/quiz/get_time_for_question",
// //   //   // dataType: "json",
// //   //   success: function (data) {
// //   //     // alert(data);
// //   //     // console.log(data);
// //   //     submit_at = data; //in seconds
// //   //   },
// //   //   error: function () {
// //   //     console.log("error");
// //   //   }
// //   // });

// //   var x = setInterval(function () {
// //     // Get today's date and time
// //     // var now = new Date().getTime();
// //     // date = new Date();
// //     // now = ((((date.getHours() * 60) + date.getMinutes()) * 60) + date.getSeconds());
// //     // if(submit_at - now < 120){
// //     //   submit_at = now + 120;
// //     // }
// //     // console.log(now)
// //     // Find the distance between now and the count down date
// //     distance = distance - 1; ///////////
// //     // console.log(distance)
// //     // Time calculations for days, hours, minutes and seconds
// //     // var days = Math.floor(distance / (1000 * 60 * 60 * 24));
// //     // var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
// //     var minutes = Math.floor(distance / 60);
// //     var seconds = Math.floor(distance - minutes * 60);

// //     // Output the result in an element with id="demo"
// //     document.getElementById("time").innerHTML = ('0'  + minutes).slice(-2)+':'+('0' + seconds).slice(-2);//minutes + "m " + seconds + "s ";
// //     // var time=('0'  + minutes).slice(-2)+':'+('0' + seconds).slice(-2);
// //     // If the count down is over, write some text 
// //     if (distance < 0) {
// //       clearInterval(x);
// //       document.getElementById("time").innerHTML = "TIME UP";
// //       document.getElementById("submit").click();
// //     }
// //   }, 1000);
// //   // alert(now);
// // })
// // $(document).ready(function () {
//   if (document.readyState === 'complete'){
//   $(document).ready(function () {
//     var distance = 120;
  
//     var x = setInterval(function () {
//       distance = distance - 1; ///////////
//       var minutes = Math.floor(distance / 60);
//       var seconds = Math.floor(distance - minutes * 60);
//       document.getElementById("time").innerHTML = ('0'  + minutes).slice(-2)+':'+('0' + seconds).slice(-2);//minutes + "m " + seconds + "s ";
//       if (distance < 0) {
//         clearInterval(x);
//         document.getElementById("time").innerHTML = "TIME UP";
//         document.getElementById("submit").click();
//       }
//     }, 1000);
//   })