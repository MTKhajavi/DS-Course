<html>
<div dir="rtl">
پیش‌نیازها <br>
مطالعه نوت‌بوک DSU <br>
</div>
<br>

<div dir="rtl">
<h1>متین و کیانوش</h1>
<br><br>
متین و کیانوش دوستان صمیمی هستند. اینقدر صمیمی که بگفته ی خودشان در همه چیز با هم
  هم نظرند. یک روز که با هم قصد سفر کرده بودند، هر کدام تصمیم گرفتند پیراهنی بپوشند که روی
  آن یک لوگو قرار دارد. این لوگو ها رشته هایی به طول n با حروف کوچک انگلیسی اند.
  ولی وقتی به هم میرسند، متوجه میشوند که لوگوهایشان با هم فرق میکنند.
<br>
  همانطور که میشد حدس زد، این اصلا براشون قابل قبول نیست. خوشبختانه یک خیاط در نزدیکی هست
  و میتواند آنها را کمک کند. خیاط به این طریق عمل میکند که 1 دلار برای هر یک زوج مرتب از حروف
  میگیرد. سپس در هر دو پیرهن، میتواند هر کدام ازین زوج مرتب ها را به هر تعداد بار که میخواهد
  با هم عوض کند.
<br>
  چون متین و کیانوش دوست ندارند پول زیادی خرج کنند، از شما میخواهند تا مینیمم پولی که باید
  خرج کنند تا پیرهن هایشان یکی بشن را بیابید.
<br>
<br><br>

<br>
  شما باید تابع solve را که n طول رشته ها و a,b که دو رشته ی n تایی هستند را میگیرد پر بکنید.
<br>
  خروجی این تابع یک دوتایی است. عضو اول مینیمم مقدار پول است.
  عضو دوم لیستی از دو تایی های حروف است که به ازای هر کدوم یدونه پول پرداخت میکنیم.
<br>
<br>
  تضمین شده است که
  n &le; 100,000
</div>
<br>

<h3 dir="rtl">مثال ها</h3>
<h4 dir="rtl">مثال 1</h4>
<pre>
<code>
n = 3
a = 'abb'
b = 'dad'
output = [2, [('a', 'd'), ('b', 'a')]]
</code>
</pre>
<h4 dir="rtl">مثال 2</h4>
<pre>
<code>
n = 8
a = 'drpepper'
b = 'cocacola'
output = [7, [('l', 'e'), ('e', 'd'), ('d', 'c'), ('p', 'c'), ('o', 'p'), ('o', 'r'), ('a', 'r')]]
</code>
</pre>

<div class="hint" dir="rtl">
  هر دو تایی که به ازایش پرداخت میکنیم را به عنوان یک یال بین آندو کاراکتر در نظر بگیرید.
</div>

<div class="hint" dir="rtl">
  اگر ('a', 'b') و ('a', 'c') را داشته باشیم جزو خرید هامون، آیا
  ('b', 'c')
  رو هم نیاز داریم؟
</div>

<div class="hint" dir="rtl">
  برای تغییر k تا حرف به هم باید حداقل k-1 دلار هزینه کنیم. (چرا؟)
</div>

<div class="hint" dir="rtl">
  هر وقت یک دو تایی اضافه میشود، مانند یک اجتماع عمل میکند. (اجتماع چه مجموعه هایی؟)
</div>

<div class="hint" dir="rtl">
  یک DSU اه 26 تایی در نظر بگیرید.
  هر وقت 2 کاراکتر توی دو رشته مساوی نبودند، باید در نهایت توی یک مجموعه باشند. پس
  اجتماع میگیریم.
</div>

</html>
