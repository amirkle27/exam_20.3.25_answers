# שאלות אמריקאיות - תבניות עיצוב (Design Patterns)
# שאלה 1
# אתם מפתחים מערכת שבה יש צורך ליצור אובייקטים מורכבים מאוד, אך תהליך היצירה מורכב ומכיל שלבים רבים. בנוסף, לעתים נדרשות גרסאות שונות של אותו אובייקט. איזה Design Pattern הכי מתאים למקרה זה?
#
# Builder Pattern
# Factory Method
# Singleton
# Prototype Pattern
print("Question 1:")
print(" "*5,"a- Builder Pattern")
# שאלה 2
# אתם מפתחים מערכת מידע שבה צריך להציג מידע במספר תצוגות שונות בו-זמנית (למשל, כגרף, כטבלה וכטקסט), וכאשר המידע מתעדכן, כל התצוגות צריכות להתעדכן אוטומטית. איזה Design Pattern הכי מתאים?
#
# Observer Pattern
# Strategy Pattern
# Command Pattern
# Mediator Pattern
print("Question 2:")
print(" "*5,"a- Observer Pattern")
# שאלה 3
# אתם מפתחים תוכנת ניהול למערכת בית חולים, ונדרש שתהיה רק מופע אחד של מנהל חיבור לבסיס הנתונים בכל המערכת כדי למנוע בעיות סנכרון וקונפליקטים בגישה לנתונים. איזה Design Pattern הכי מתאים?
#
# Facade Pattern
# Proxy Pattern
# Singleton Pattern
# Command Pattern
print("Question 3:")
print(" "*5,"c- Singleton Pattern")
# שאלה 4
# אפליקציית מסחר אלקטרוני מנהלת הזמנות שעוברות בין מצבים שונים: "חדשה", "מאושרת", "נשלחה", "התקבלה" ו"בוטלה". בכל מצב יש פעולות שונות שניתן לבצע על ההזמנה (למשל, הזמנה במצב "חדשה" ניתנת לעריכה, אך הזמנה "נשלחה" לא). איזה Design Pattern הכי מתאים ליישום התנהגות זו?
#
# State Pattern
# Observer Pattern
# Mediator Pattern
# Chain of Responsibility Pattern
print("Question 4:")
print(" "*5,"a- State Pattern")
# שאלה 5
# אתם מפתחים מערכת ניתוח נתונים שצריכה לבצע שרשרת של צעדי עיבוד על קבצים שונים. צעדי העיבוד כוללים קריאת קובץ, סינון נתונים, עיבוד סטטיסטי והצגת תוצאות. המסגרת הכללית של התהליך אחידה, אך הפרטים של כל שלב משתנים בהתאם לסוג הקובץ ולדרישות הניתוח. איזה Design Pattern הכי מתאים?
#
# Template Method Pattern
# Chain of Responsibility Pattern
# Command Pattern
# Iterator Pattern
print("Question 5:")
print(" "*5,"a- Template Method Pattern")
# שאלה 6
# אתם בונים מערכת ניהול לספרייה דיגיטלית שכוללת ממשקים מורכבים לחיפוש, הורדה, ניהול מנויים ותשלומים. המפתחים החדשים במערכת מתקשים להבין את כל המורכבות, ואתם רוצים לספק להם ממשק פשוט שיסתיר את המורכבות הפנימית. איזה Design Pattern הכי מתאים?
#
# Adapter Pattern
# Facade Pattern
# Composite Pattern
# Bridge Pattern
print("Question 6:")
print(" "*5,"b- Facade Pattern")
# שאלה 7
# אתם מפתחים מערכת עיצוב גרפי שבה משתמשים יכולים להוסיף אפקטים שונים לתמונות (כמו פילטרים, מסגרות, כיתוב וכו'). אתם רוצים לאפשר למשתמשים להוסיף ולהסיר אפקטים באופן דינמי בזמן ריצה, מבלי לשנות את האובייקט המקורי של התמונה. איזה Design Pattern הכי מתאים?
#
# Decorator Pattern
# Proxy Pattern
# Adapter Pattern
# Composite Pattern
print("Question 7:")
print(" "*5,"a- Decorator Pattern")
# שאלה 8
# אתם מפתחים מערכת אבטחה שמנתחת בקשות גישה למידע רגיש. כל בקשה צריכה לעבור דרך שרשרת של בדיקות אבטחה (אימות משתמש, בדיקת הרשאות, בדיקת מיקום גיאוגרפי, זיהוי פעילות חשודה). כל בדיקה יכולה לאשר את הבקשה, לדחות אותה, או להעביר אותה לבדיקה הבאה. איזה Design Pattern הכי מתאים?
#
# Command Pattern
# Chain of Responsibility Pattern
# Template Method Pattern
# Interpreter Pattern
print("Question 8:")
print(" "*5,"b- Chain of Responsibility Pattern")
# שאלה 9
# אתם מפתחים מערכת לעיבוד תמונות שצריכה לתמוך במגוון רחב של אובייקטים - החל מתמונות בודדות ועד לאלבומים שלמים המכילים תיקיות משנה ותמונות נוספות. המערכת צריכה לטפל בכל המבנים הללו באופן אחיד (למשל, לבצע עיבוד כמו שינוי בהירות על תמונה בודדת או על אלבום שלם). איזה Design Pattern הכי מתאים?
#
# Adapter Pattern
# Composite Pattern
# Proxy Pattern
# Bridge Pattern
print("Question 9:")
print(" "*5,"b- Composite Pattern")
# שאלה 10
# אתם מפתחים מערכת לייצור רכיבי תוכנה שונים (כמו כפתורים, שדות טקסט, רשימות נפתחות) שצריכים להתאים לפלטפורמות שונות (Windows, macOS, Linux) תוך שמירה על מראה והתנהגות עקביים לכל פלטפורמה. אתם צריכים ליצור משפחות של אובייקטים קשורים מבלי לציין את המחלקות הקונקרטיות שלהם. איזה Design Pattern הכי מתאים?
#
# Factory Method
# Abstract Factory
# Builder Pattern
# Prototype Pattern
print("Question 10:")
print(" "*5,"b- Abstract Factory")
# שאלה 11
# אתם מפתחים אפליקציית ניווט וחייבים להשתמש במערכות מיקום שונות (GPS, סלולרי, WiFi). המודולים שמפעילים כל טכנולוגיית מיקום פותחו על-ידי צוותים שונים, ולכל מודול יש ממשק תכנות שונה לגמרי. אתם רוצים שהאפליקציה תעבוד מול ממשק אחיד בלי להתעסק בהבדלים בין הממשקים של הטכנולוגיות השונות. איזה Design Pattern הכי מתאים?
#
# Factory Method
# Iterator Pattern
# Facade Pattern
# Flyweight Pattern
print("Question 11:")
print(" "*5,"c- Facade Pattern")
# שאלה 12
# בעת פיתוח אפליקציית מסרים, אתם צריכים ליצור מנגנון שיאפשר לשלוח הודעות במספר דרכים (SMS, דוא"ל, הודעה בתוך האפליקציה), כאשר כל אחת מהדרכים מיושמת באופן שונה לחלוטין. אתם רוצים לאפשר להחליף בין שיטות שליחה מבלי לשנות את הקוד שמשתמש בהן. איזה Design Pattern הכי מתאים?
#
# Strategy Pattern
# Adapter Pattern
# Factory Method
# Template Method Pattern
print("Question 12:")
print(" "*5,"a- Strategy Pattern")
# שאלה 13
# אתם עובדים על שירות API שצריך להגביל את מספר הבקשות שכל משתמש יכול לשלוח בפרק זמן מסוים. אתם רוצים להוסיף שכבת אבטחה זו מבלי לשנות את קוד השירות הקיים. איזה Design Pattern הכי מתאים?
#
# Proxy Pattern
# Decorator Pattern
# Adapter Pattern
# Bridge Pattern
print("Question 13:")
print(" "*5,"a- Proxy Pattern")
# שאלה 14
# אתם מפתחים מחולל מבוכים למשחק תפקידים, ורוצים לאפשר סריקה שיטתית של כל החדרים והמעברים במבוך שנוצר. המבנה הפנימי של המבוך מורכב ומכיל אוספים שונים של אובייקטים, אבל אתם רוצים לספק למשתמש דרך פשוטה ואחידה לעבור על כל אלמנטי המבוך ללא צורך בהבנת המבנה הפנימי שלו. איזה Design Pattern הכי מתאים?
#
# Visitor Pattern
# Iterator Pattern
# Observer Pattern
# Prototype Pattern
print("Question 14:")
print(" "*5,"b- Iterator Pattern")
# שאלה 15
# אתם מפתחים משחק RPG בו השחקנים יכולים ליצור דמויות עם מראה ותכונות מותאמות אישית. השחקנים בוחרים גזע (אדם, אלף, גמד), מקצוע (לוחם, קוסם, גנב), ומגוון של מאפיינים נוספים. במקום לבנות מראש את כל האפשרויות האפשריות (שהן מספר עצום), אתם רוצים לאפשר שכפול של דמויות קיימות ואז התאמה של המאפיינים הספציפיים. איזה Design Pattern הכי מתאים?
#
# Factory Method
# Prototype Pattern
# Abstract Factory
# Builder Pattern
print("Question 15:")
print(" "*5,"b- Prototype Pattern")