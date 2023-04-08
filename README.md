# ijara_uz
Assalomu alaikum ushbu IJARA_UZ web sayti uchun tuzilgan backend bo'lib,
quidagi qisimlarni o'z ichiga oladi:

~ Ushbu sayt asosan talabalar foydalanishi uchun mo'ljallangan bo'lib barcha web saytlarda bo'lgani kabi ro'yxatdan
o'tish qismini o'z ichiga oladi: https://_____/api/register (methods: "POST")

~ Talabalar uchun kvartiralar e'loni va talabalar ushbu e'lonlarni filterlar(for_men, is_flat, contract) yourdamida 
qidirish imkoniyatiga ega bo'ladilar:
https://_____/api/apartment/ -- (methods: "GET", "POST")
https://_____/api/apartment/<int:pk> (methods: "GET", "PUT")
https://_____/api/apartment/search/?query=<str>&is_flat=<bool>&for_men:<bool>&contract=<bool> (methods: "GET")

~ Talabalar uchun ish e'lonlari joylash va ko'rish imkoiyatlari:
https://_____/api/jobs/ -- (methods: "GET", "POST")
https://_____/api/jobs/ -- (methods: "GET", "PUT")
https://_____/api/jobs/search/?query=<str> (methods: "GET")

~ WEB saytning "POST" metodlari faqatgina ro'yhatdan o'tgan userlar uchun bo'lib Djoser Authentication yordamida Tokenli avtarizatsiya qo'anilgan:
http://____/api/auth/token/login (methods: "POST")
http://____/api/auth/token/logout (methods: "POST")
