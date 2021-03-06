"""
[(difficulty(E,M,H), que_no, group(S,C),
 ques, ans),]
"""
data = [
('E',1,'C','SetA={1,3,5,7……297,299—150 Odd numbers}. In how many ways are there to choose exactly 18 numbers from set A such that their sum is 191?','0'),
('E',2,'C','We have a 50 ft piece of rope. If it takes one second to cut it into a 1-foot piece. How long would it take to cut the entire rope into one-foot pieces?','49'),
('E',3,'C','The ratio of employees to managers is 7: 3. 70% of the employees and 30% of the managers take lunch in the canteen. What % of total workforce takes lunch in canteen?','58'),
('E',4,'C','Mangleshacharya was born in 1357 B.C. He had lived one-third of his life as a boy, one-fifth of his life as a youth, one-fourth of his life as a man and the remaining 39 years as an old man. What was his age when he died?','180'),
('E',5,'C','If two similar triangles have bases in the ratio of 3:4, what is the ratio of their areas?','9:16'),
('E',6,'C','What is the four-digit number in which the first digit is1/4 of the second, the third is the sum of the first and second, and the last is two times the second?','1458'),
('E',7,'C','What is the smallest number which when divided by 35 leaves remainder 30, when divided by 45 leaves remainder 40 and when divided by 55 leaves remainder 50?','3460'),
('E',8,'C','Hari\'s age is three years more than four times Rakesh\'s age. After five years, Hari\'s age will be one year more than thrice Rakesh\'s age. What is Hari\'s present age?','35'),
('E',9,'C','The difference in simple interest and compound interest on a certain sum of money in 2 years at 10% p.a. is Rs. 50. The sum is?','5000'),
('E',10,'C','The length of the longest rod which can fit into a cubical room of 5 m side is', '12:11'),
('E',11,'C','How long will it take to row 20 km upstream if one can row 10 km in 10 minutes in still water and the same distance in 8 minutes with the stream?','26.67'),
('E',12,'C','I invested a sum of money at compound interest. It amounted to Rs. 6741 in 3 years and Rs. 6420 in 4 years. Find the rate of interest.','5'),
('E',13,'C','A certain number of men can complete a piece of work in 180 days. If there are 30 men less, it will take 20 days more for the work to be completed. How many men were there originally?','300'),
('E',14,'C','In what ratio must two kinds of sugar at Rs. 1.15 and Rs. 1.24 per kg be mixed so that by selling at Rs. 1.50 per kg, 25% may be gained?','4:5'),
('E',15,'C','How much sugar at Rs. 9.5 a kg should be added to 17 kg of tea at Rs. 20 a kg so that the mixture be worth Rs. 13 a kg.?','34'),
('E',16,'C','In the General meeting of \'Bulls Eye Society\', Poonam said, \'The repairs to the Society will come to a total of Rs 3120 and I recommend that this amount should be met by the members, each paying an equal amount.\' The recommendation was immediately agreed. However, four members of the Society chose to resign, leaving the remaining members to pay an extra Rs 26 each. How many members did the Society originally have?','24'),

('M',1,'C','The height of a certain flagpole is 33feet. Grease is applied to the pole. A Monkey attempts to climb the pole . It climbs 5 feet every second but slips down 4ft in the next second. When will the monkey reach the top of the flagpole?','57'),
('M',2,'C','In the following question one term in the number series is worng, find out the wrong term. 1,3,12,25,48','25'),
('M',3,'C','Rajat appeared for a Science exam. He was given 135 problems to solve. He tried to solve all of them correctly but some of them went wrong. Anyhow he scored 75. His score was calculated by subtracting three times the number of wrong answers from the number of correct answers. Can you tell how many problems he solved correctly?','120'),
('M',4,'C','When a student weighing 54 kg left a class, the average weight of the remaining 59 students increased by 100g. What is the average weight of the remaining 59 students?','60'),
('M',5,'C','A number of 5 digits have the following properties: The number comprising the leftmost two digits is divisible by 2, that comprising the leftmost three digits is divisible by 3, the leftmost four by 4, the leftmost five by 5. Each digit in the number is different i.e. no digits are repeated. The digit 0 does not occur in the number i.e. it is comprised only of the digits 5-9 in some order. How many such numbers are possible and find their value/values?','78965'),
('M',6,'C','Rahul invested Rs. 70000 in a bank at the rate of 6.5% p.a. simple interest rate. He recieved Rs. 85925 after the end of the term. Find out the period for which the sum was invested by Rahul?','3.5'),
('M',7,'C','A man is paid Rs. 240 plus one coat for one-year service. However, he left after 9 months and receives Rs. 150 and a coat. Then find the price of the coat.','120'),
('M',8,'C','Barbara visited her High School friend, Natasha after their 25th school reunion. \'What a nice pair of children you have, are they twins?\', Barbara asked. \'No my sister is older than I\', said Natasha’s son Philip. \'The square of my age plus the cube of her age is 7148\'. \'The square of my age plus the cube of his age is 5274\', said Matilda. What is Matilda’s age?','19'),
('M',9,'C','A square with side 8 cm is divided into small squares with side 1 cm each. How many squares are there in all?','204'),
('M',10,'C','In a casino, Anurag bets on number 23 on a spinning wheel 12 times and loses each time. On the 13th spin he does a quick calculation and finds out that the number 17 had appeared three times in the last 12 spins and is therefore, unable to decide whether to bet on 23 or 17 in the 13th spin. Which number (23 or 17) will give him the best chance of winning and what are the odds of winning on the bet that he takes? (Wheel has numbers 1 to36)','35:1'),
('M',11,'C','Neeti puts into the basket one banana when ordered ‘one’, one kiwi when ordered ‘Two’, one litchi when ordered ‘Three’, and is asked to take out from the basket one banana and kiwi when asked Four. A sequence of order is given as: 12342231124124213 How many total fruits will be in the basket at the end of the above order sequence?','8'),
('M',12,'C','An elephant and a tiger were carrying full sacks on their backs. The elephant started complaining that his load was too heavy. The tiger said to him "Why are you complaining? If you gave me one of your sacks I\'d have double what you have and if I give you one of my sacks we\'d have an even amount." What is the minimum number of sacks the elephant is carrying?','5 sacks'),
('M',13,'C','If Etti can swim 4 miles downstream (with the current) in a river in 20 minutes, & upstream 1 mile (against the current) in 15 minutes, how long would it take her to swim a mile in still water?','7.5'),
('M',14,'C','A man is standing on the deck of a ship, which is 10m above water level. He observes the angle of elevation of the top of a light house as 600 and the angle of depression of the base of lighthouse as 300. Find the height of the light house','40'),
('M',15,'C','The value of (sin 39°) / (cos 51°) + 2 tan11° tan31° tan45° tan59° tan79° – 3 (sin2 21° + sin2 69°) is?','0'),
('M',16,'C','The gradient of the curve y=2(x^3)-3(x^2)-12x+8 at x=0 is','12'),
('M',17,'C','The sum of the incomes of Arya and Beck is more than that of Caroline and Damon together. The sum of the Incomes of Arya and Caroline is the same as that of Beck and Damon taken together.Moreover, Arya earns half as much as the sum of the incomes of Beck and Damon? Whose income is the highest?','Beck'),

('H',1,'C','A Pizza delivery boy named Mahesh wanted to give 20 pizzas to the office. He had bags which can carry a maximum of 10 pizzas. There were ten guards standing at different positions near the office. Each guard would take one pizza from each of the bag. (i.e. if the Delivery boy carries 2 bags, and there are say 10 pizzas in each bag, the first guard would take 1 from each bag i.e. total of 2. And all other guards would do this.) In order to give 20 pizzas to the office, how any minimum pizzas the delivery boy should carry?','66'),
('H',2,'C','An eagle is flying between two trains, each travelling towards each other on the same track at 80 km/h. The eagle reaches one engine, reverses itself immediately, and flies back to the other engine, repeating the process each time. The eagle is flying at 50 km/h. If the eagle flies 150 km before the trains meet, how far apart were the trains initially?','148'),
('H',3,'C','Sagrika multiplied 414 by certain number and obtained 69958 as the answer. But she found that there is some error in the answer - both the 9s in the answer are wrong and all the other digits are correct. Can you find the correct answer? ','60858'),
('H',4,'C','1000 cats were kept under observation to check their growth rates. After six months, there were 1000R cats. At the beginning of the 3rd year, there were roughly 2828R cats, which was 4 times what the scientists placed in there at the beginning of the 1st year. If R is a positive variable, how many cats would be there at the beginning of the 11th year?','102400'),
('H',5,'C','A thief wants to open a lock with 5 digits as the key to open it. He knows that the 3rd digit is three less than 2nd digit, while 2nd digit is four smaller than 4th digit. The first digit is three times the fifth digit. There are three pairs whose sum is 11 and third and fifth digits are equal. Find the key to open the lock','65292'),
('H',6,'C','If ABCDE*4=EDCBA If A, B, C, D and E represent diﬀerent numbers, and none of them is zero, then what number is ABCDE?','21978'),
('H',7,'C','If cosθ = – 1/2 and π < θ < 3π, find the value of 4 tan2θ– 3 cosec2θ 2 ','8'),
('H',8,'C','True or False. If lim f(x) and lim g(x) exist as x approaches a then lim [ f(x) / g(x) ] = lim f(x) / lim g(x) as x approaches a.','False'),
('H',9,'C','The difference between simple and compound interest(compounded annually) on a certain sum of money for 2 years at 4% per annum is Rs.1. What is the sum?','625'),
('H',10,'C','The price of 80 apples is equal to that of 120 oranges. The price of 60 apples and 75 oranges together is Rs. 1320. The total price of 25 apples and 40 oranges is?','620'),
('H',11,'C','A contract is to be completed in 56 days if 104 persons work, each working at 8 hours a day. After 30 days, 25 of the work is completed. How many additional persons should be deployed so that the work will be completed in the scheduled time, each persons now working 9 hours a day?','56'),
('H',12,'C','A starts a business with Rs.40,000. After 2 months, B joined him with Rs.60,000. C joined them after some more time with Rs.1,20,000. At the end of the year, out of a total profit of Rs.3,75,000, C gets Rs.1,50,000 as his share. How many months after B joined the business, did C join?','4'),
('H',13,'C','A, B and C jointly thought of engaging themselves in a business venture. It was agreed that A would invest Rs. 6500 for 6 months, B, Rs. 8400 for 5 months and C, Rs. 10,000 for 3 months. A wants to be the working member for which, he was to receive 5% of the profits. The profit earned was Rs. 7400. What is the share of B in the profit?','2660'),
('H',14,'C','A man buys Rs. 20 shares paying 9% dividend. The man wants to have an interest of 12% on his money. What is the market value of each share?','15'),
('H',15,'C','A bag contains 2 white balls, 3 black balls and 4 red balls. In how many ways can 3 balls be drawn from the bag, if at least one black ball is to be included in the draw?','64'),
('H',16,'C','A train is running at a speed of 4040 km/hr and it crosses a post in 1818 seconds. What is the length of the train?','200'),

('E',1,'S','What would be the difference between the place values of the digits at the tens and units places of a number formed by the addition of the greatest six-digit number and the smallest three-digit number?','81'),
('E',2,'S','(112* 54)=?','70000'),
('E',3,'S','A three-digit number 4a3 is added to another three-digit number 984 to give a four digit number 13b7, which is divisible by 11. What is the value of (a + b)?','10'),
('E',4,'S','A man has Rs.480 in the denominations of one-rupee notes, five-rupee notes and ten-rupee notes. The number of notes of each denomination is equal. What is the total number of notes that he has ?','90'),
('E',5,'S','Ratio of the present ages of two brothers is 4:5. After 10 years, the ratio of their ages would be 6:7. Find the age of the elder brother after 15 years.','40'),
('E',6,'S','An error 2%  in excess is made while measuring the side of a square. What is the percentage of error in the calculated area of the square?','4.04'),
('E',7,'S','If the diagonals of a rhombus are 24 cm and 10 cm, what is its perimeter?','52'),
('E',8,'S','A is two years older than B who is twice as old as C. The total of the ages of A, B and C is 27. How old is B?','10'),
('E',9,'S','The difference between a positive fraction and its reciprocal is 9/20. Find the sum of that fraction and its reciprocal.','2.05'),
('E',10,'S','109 × 109 + 91 × 91 = ?','20162'),
('E',11,'S','Reena took a loan of Rs. 1200 with simple interest for as many years as the rate of interest. If she paid Rs. 432 as interest at the end of the loan period, what was the rate of interest?','6'),
('E',12,'S','What is the multiplicative inverse of the product when 12/17 is multiplied by the reciprocal of  21/34?','0.88'),
('E',13,'S','(3+2p) and (5+3q) are the digits in the thousands and tens places repectively of the number 84527. Find the values of p.','0.5'),
('E',14,'S','1531×132+1531×68=?','306200'),
('E',15,'S','476A50 is divisible by both 3 and 11. What is the non-zero digits in the hundred\'s places?','8'), 

('M', 1,'S','What will be the sum of adding all the possible three-digit numbers formed by 7, 2, 5 using each of the digits only once?','3108'),
('M', 2,'S','How many prime numbers from 11 to 100 are there, whose digits when interchanged give a prime number?','9'),
('M', 3,'S','The price of 2 sarees and 4 shirts is Rs. 1600. With the same money one can buy 1 saree and 6 shirts. If one wants to buy 12 shirts, how much shall he have to pay ?','2400'),
('M', 4,'S','143×72 / 98 = ?','1372'),
('M', 5,'S','What is the unit digit in (6324)^1797×(615)^316×(341)^467','0'),
('M', 6,'S','(912+643)2+(912−643)2 / (912×912+643×643) =?','2'),
('M', 7,'S','If Z = 52 and ACT = 48, then BAT will be equal to','46'),
('M', 8,'S','12 workers can complete a piece of work in 10 days. If the number of workers are reduced to 1/3rd the original number, then how many more days would be required to complete the same work?','20'),
('M', 9,'S','Find the next number in the sequence: 190, 94, 46, 22, 10, 4?','1'),
('M', 10,'S','The ratio between the speeds of two trains is 7:8. If the second train runs 400 kms in 4 hours, then what is the speed of the first train?','87.5'),
('M', 11,'S','Father is aged three times more than his son Sunil. After 8 years, he would be two and a half times of Sunil\'s age. After further 8 years, how many times would he be of Sunil\'s age?','2'),
('M', 12,'S','In a shop, there are 4 dolls of different heights P,Q,R and S. S is neither as tall as P nor as short as R. Q is shorter than S but taller than R. If Kittu wants to purchase the tallest doll, which one should she purchase?','P'),
('M', 13,'S','Find the missing number in the series? 4, 18, ?, 100, 180, 294, 448','48'),
('M', 14,'S','A sum of Rs. 1360 has been divided among A, B and C such that A gets 2/3rd of what B gets and B gets 1/4th of what C gets. B\'s share is','240'),
('M', 15,'S','The area of a rectangular plot is 460 square metres. If the length is 15% more than the breadth, what is the breadth of the plot?','20'),
('M', 16,'S','(422+404)2−(4×422×404)=?','324'),
('M', 17,'S','In a family, there are six members A, B, C, D, E, F. A and B are a married couple, A being the male member. D is the only son of C, who is the brother of A. E is the sister of D. B is the daughter-in-law of F, whose husband has died. How is E related to C?','Daughter'),

('H',  1,'S','A fort had provision of food for 150 men for 45 days. After 10 days, 25 men left the fort. The number of days for which the remaining food will last, is?','42'),
('H',  2,'S','What is the greatest number which divides 639, 1065 and 1491 exactly?','213'),
('H',  3,'S','If a number is divided by 6, 3 is the remainder . What is the remainder if the the square of the number is divided by 6?','3'),
('H',  4,'S','Ayisha\'s age is 1/6th of her father\'s age. Ayisha\'s father\'s age will be twice Shankar\'s age after 10 years. If Shankar\'s eight birthdays was celebrated two years before, then what is Ayisha\'s present age?','5'),
('H',  5,'S','A rectangular park 60 metre long and 40 metre wide has two concrete crossroads running in the middle of the park and rest of the park has been used as a lawn. The area of the lawn is 2109 square metre. What is the width of the road?','3'),
('H',  6,'S','One-third of Rahul\'s savings in National Savings Certificate is equal to one-half of his savings in Public Provident Fund. If he has Rs. 1,50,000 as total savings, how much has he saved in Public Provident Fund ?','60000'),
('H',  7,'S','The average salary of all the workers in a workshop is Rs. 8000. The average salary of 7 technicians is Rs. 12000 and the average salary of the rest is Rs. 6000. How many workers are there in the workshop?','21'),
('H',  8,'S','A large field of 700 hectares is divided into two parts. The difference of the areas of the two parts is one-fifth of the average of the two areas. What is the area of the smaller part in hectares?','315'),
('H',  9,'S','A tank is 25 metre long, 12 metre wide and 6 metre deep. What is the cost of plastering its walls and bottom at the rate of  75 paise per square metre?','558'),
('H', 10,'S','A hall is 15m long and 12m broad. If the sum of the areas of the floor and ceiling is equal to the sum of the areas of the four walls, the volume of the hall is?','1200'),
('H', 11,'S','The difference of the squares of two consecutive even integers is always divisible by','4'),
('H', 12,'S','If the rational numbers 2/5, 5/8, 4/7, 7/10 are are arranged in the ascending order, what will be the square of the second last fraction? (Answer in fraction format in simplified form. Example: a/b)','16/49'),
('H', 13,'S','What is the sum of the natural numbers from 21 to 50?','1065'),
('H', 14,'S','A fires 5 shots to B\'s 3 but A kills only once in 3 shots while B kills once in 2 shots. When B has missed 27 times, A has killed','30'),
('H', 15,'S','Find out the smallest number which when divided by any number from 2 to 10, the remainder will be 1.','2521'),
('H', 16,'S','The square root of [(8×9×10×11)+1]=?','89'),
('H', 17,'S','How many four-digit perfect square numbers have 4, 5 or 6 in their units place?','35'),
('H', 18,'S','39 persons can repair a road in 12 days, working 5 hours a day. In how many days will 30 persons, working 6 hours a day, complete the work?','13'),
]

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','que.settings')

import django
django.setup()

from quiz.models import Qna


def populate_quiz():
	for d in data:
		diff 	= d[0]
		que_no 	= d[1]
		grp 	= d[2]
		que 	= d[3]# + ' [(Answer: ' + d[4] + ') - ' + diff + str(que_no)+']'
		ans 	= d[4]

		grp_code = 1 if grp=='S' else 2
		diff_code = 1 if diff=="E" else (2 if diff=="M" else 3)
		que_id = grp_code*10000 + diff_code*1000 + que_no

		entry = Qna(difficulty=diff,
			q_no=que_no,
			question=que,
			answer=ans,
			group=grp,
			qid=que_id)
		entry.save()

populate_quiz()
print('done')