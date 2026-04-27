from app import app
from database.db import db
from models.question import Question

with app.app_context():

    questions = [

# =========================
# 🔢 APTITUDE - NUMBERS
# =========================

Question(question="2+2=?", option1="3", option2="4", option3="5", option4="6",
         answer="4", category="aptitude", topic="numbers", difficulty="easy"),

Question(question="5×6=?", option1="30", option2="25", option3="35", option4="40",
         answer="30", category="aptitude", topic="numbers", difficulty="easy"),

Question(question="12×12=?", option1="124", option2="144", option3="154", option4="164",
         answer="144", category="aptitude", topic="numbers", difficulty="medium"),

Question(question="Square root of 256?", option1="12", option2="14", option3="16", option4="18",
         answer="16", category="aptitude", topic="numbers", difficulty="medium"),

Question(question="What is 25% of 200?", option1="25", option2="50", option3="75", option4="100",
         answer="50", category="aptitude", topic="numbers", difficulty="easy"),

Question(question="LCM of 4 and 6?", option1="12", option2="24", option3="6", option4="18",
         answer="12", category="aptitude", topic="numbers", difficulty="medium"),

Question(question="HCF of 12 and 18?", option1="6", option2="3", option3="9", option4="12",
         answer="6", category="aptitude", topic="numbers", difficulty="medium"),

Question(question="What is 7²?", option1="42", option2="49", option3="56", option4="64",
         answer="49", category="aptitude", topic="numbers", difficulty="easy"),

Question(question="Cube of 3?", option1="6", option2="9", option3="27", option4="81",
         answer="27", category="aptitude", topic="numbers", difficulty="easy"),

Question(question="100 ÷ 4=?", option1="20", option2="25", option3="30", option4="40",
         answer="25", category="aptitude", topic="numbers", difficulty="easy"),


# =========================
# 💰 APTITUDE - PROFIT LOSS
# =========================

Question(question="CP=100, SP=120. Profit?", option1="10", option2="20", option3="30", option4="40",
         answer="20", category="aptitude", topic="profit_loss", difficulty="easy"),

Question(question="CP=200, SP=150. Loss?", option1="25", option2="50", option3="75", option4="100",
         answer="50", category="aptitude", topic="profit_loss", difficulty="easy"),

Question(question="Profit % if CP=100 SP=150?", option1="25%", option2="50%", option3="75%", option4="100%",
         answer="50%", category="aptitude", topic="profit_loss", difficulty="medium"),

Question(question="Loss % if CP=500 SP=400?", option1="10%", option2="20%", option3="25%", option4="30%",
         answer="20%", category="aptitude", topic="profit_loss", difficulty="medium"),

Question(question="SP when CP=100, Profit 20%?", option1="110", option2="120", option3="130", option4="140",
         answer="120", category="aptitude", topic="profit_loss", difficulty="medium"),

Question(question="CP when SP=120, Profit 20%?", option1="100", option2="90", option3="80", option4="110",
         answer="100", category="aptitude", topic="profit_loss", difficulty="hard"),

Question(question="Marked price=200, discount 10%. SP?", option1="180", option2="170", option3="160", option4="150",
         answer="180", category="aptitude", topic="profit_loss", difficulty="easy"),

Question(question="Profit of 25% on CP 200?", option1="50", option2="40", option3="30", option4="60",
         answer="50", category="aptitude", topic="profit_loss", difficulty="easy"),

Question(question="Loss of 10% on 500?", option1="40", option2="50", option3="60", option4="70",
         answer="50", category="aptitude", topic="profit_loss", difficulty="easy"),

Question(question="SP if CP=300, loss 20%?", option1="240", option2="250", option3="260", option4="270",
         answer="240", category="aptitude", topic="profit_loss", difficulty="medium"),


# =========================
# 🧠 REASONING - ANALOGY
# =========================

Question(question="Dog : Bark :: Cat : ?", option1="Meow", option2="Roar", option3="Growl", option4="Cry",
         answer="Meow", category="reasoning", topic="analogy", difficulty="easy"),

Question(question="Bird : Fly :: Fish : ?", option1="Swim", option2="Run", option3="Jump", option4="Walk",
         answer="Swim", category="reasoning", topic="analogy", difficulty="easy"),

Question(question="Pen : Write :: Knife : ?", option1="Cut", option2="Draw", option3="Read", option4="Erase",
         answer="Cut", category="reasoning", topic="analogy", difficulty="easy"),

Question(question="Car : Drive :: Plane : ?", option1="Fly", option2="Run", option3="Move", option4="Travel",
         answer="Fly", category="reasoning", topic="analogy", difficulty="easy"),

Question(question="Teacher : Teach :: Doctor : ?", option1="Treat", option2="Learn", option3="Help", option4="Guide",
         answer="Treat", category="reasoning", topic="analogy", difficulty="medium"),

Question(question="Book : Read :: Food : ?", option1="Eat", option2="Cook", option3="Drink", option4="Serve",
         answer="Eat", category="reasoning", topic="analogy", difficulty="easy"),

Question(question="Sun : Day :: Moon : ?", option1="Night", option2="Sky", option3="Light", option4="Dark",
         answer="Night", category="reasoning", topic="analogy", difficulty="easy"),

Question(question="King : Queen :: Man : ?", option1="Woman", option2="Girl", option3="Lady", option4="Child",
         answer="Woman", category="reasoning", topic="analogy", difficulty="easy"),

Question(question="Wheel : Car :: Wing : ?", option1="Bird", option2="Plane", option3="Fan", option4="Helicopter",
         answer="Bird", category="reasoning", topic="analogy", difficulty="medium"),

Question(question="Finger : Hand :: Toe : ?", option1="Leg", option2="Foot", option3="Body", option4="Head",
         answer="Foot", category="reasoning", topic="analogy", difficulty="easy"),


# =========================
# 🔢 REASONING - SERIES
# =========================

Question(question="2,4,6,8,?", option1="10", option2="12", option3="14", option4="16",
         answer="10", category="reasoning", topic="series", difficulty="easy"),

Question(question="1,3,6,10,?", option1="12", option2="15", option3="18", option4="20",
         answer="15", category="reasoning", topic="series", difficulty="medium"),

Question(question="5,10,20,40,?", option1="60", option2="80", option3="100", option4="120",
         answer="80", category="reasoning", topic="series", difficulty="easy"),

Question(question="3,9,27,?", option1="54", option2="81", option3="108", option4="72",
         answer="81", category="reasoning", topic="series", difficulty="easy"),

Question(question="2,3,5,7,?", option1="9", option2="11", option3="13", option4="15",
         answer="11", category="reasoning", topic="series", difficulty="medium"),

Question(question="4,6,9,13,?", option1="16", option2="17", option3="18", option4="19",
         answer="18", category="reasoning", topic="series", difficulty="hard"),

Question(question="10,20,30,?", option1="40", option2="50", option3="60", option4="70",
         answer="40", category="reasoning", topic="series", difficulty="easy"),

Question(question="7,14,28,?", option1="35", option2="42", option3="56", option4="60",
         answer="56", category="reasoning", topic="series", difficulty="easy"),

Question(question="1,4,9,16,?", option1="20", option2="25", option3="30", option4="36",
         answer="25", category="reasoning", topic="series", difficulty="medium"),

Question(question="2,6,7,21,22,?", option1="66", option2="44", option3="33", option4="55",
         answer="66", category="reasoning", topic="series", difficulty="hard"),



#logical reasoning
Question(question="If CAT = DBU, then DOG = ?", option1="EPH", option2="FQI", option3="EPI", option4="DOH",
         answer="EPH", category="reasoning", topic="coding", difficulty="medium"),

Question(question="If PEN = QFO, then MAP = ?", option1="NBQ", option2="MBQ", option3="NBR", option4="LBP",
         answer="NBQ", category="reasoning", topic="coding", difficulty="medium"),

Question(question="If A=1, B=2, then CAT = ?", option1="24", option2="26", option3="25", option4="27",
         answer="24", category="reasoning", topic="coding", difficulty="easy"),

Question(question="If DOG = 4157, then GOD = ?", option1="7415", option2="7541", option3="1574", option4="4517",
         answer="7415", category="reasoning", topic="coding", difficulty="hard"),


Question(question="A man walks 10m north, then 5m east. Where is he now?", option1="North-East", option2="South-East", option3="North-West", option4="South-West",
         answer="North-East", category="reasoning", topic="direction", difficulty="easy"),

Question(question="A walks south, then turns left. Which direction now?", option1="East", option2="West", option3="North", option4="South",
         answer="East", category="reasoning", topic="direction", difficulty="easy"),

Question(question="Facing north, turn right then right again. Direction?", option1="South", option2="East", option3="West", option4="North",
         answer="South", category="reasoning", topic="direction", difficulty="medium"),

Question(question="A man walks 10m north, then 5m east. Where is he now?", option1="North-East", option2="South-East", option3="North-West", option4="South-West",
         answer="North-East", category="reasoning", topic="direction", difficulty="easy"),

Question(question="A walks south, then turns left. Which direction now?", option1="East", option2="West", option3="North", option4="South",
         answer="East", category="reasoning", topic="direction", difficulty="easy"),

Question(question="Facing north, turn right then right again. Direction?", option1="South", option2="East", option3="West", option4="North",
         answer="South", category="reasoning", topic="direction", difficulty="medium"),


#verbal ability

Question(question="Synonym of 'Rapid'?", option1="Slow", option2="Fast", option3="Weak", option4="Late",
         answer="Fast", category="verbal", topic="synonym", difficulty="easy"),

Question(question="Synonym of 'Happy'?", option1="Sad", option2="Joyful", option3="Angry", option4="Tired",
         answer="Joyful", category="verbal", topic="synonym", difficulty="easy"),

Question(question="Synonym of 'Big'?", option1="Small", option2="Huge", option3="Tiny", option4="Short",
         answer="Huge", category="verbal", topic="synonym", difficulty="easy"),
Question(question="Antonym of 'Hot'?", option1="Warm", option2="Cold", option3="Cool", option4="Heat",
         answer="Cold", category="verbal", topic="antonym", difficulty="easy"),

Question(question="Antonym of 'Easy'?", option1="Simple", option2="Hard", option3="Soft", option4="Light",
         answer="Hard", category="verbal", topic="antonym", difficulty="easy"),

Question(question="Antonym of 'Early'?", option1="Late", option2="Soon", option3="Fast", option4="Quick",
         answer="Late", category="verbal", topic="antonym", difficulty="easy"),
Question(question="She ___ to school daily.", option1="go", option2="goes", option3="gone", option4="going",
         answer="goes", category="verbal", topic="fill_blank", difficulty="easy"),

Question(question="He ___ playing cricket.", option1="is", option2="are", option3="am", option4="be",
         answer="is", category="verbal", topic="fill_blank", difficulty="easy"),

Question(question="They ___ finished their work.", option1="has", option2="have", option3="had", option4="having",
         answer="have", category="verbal", topic="fill_blank", difficulty="easy"),
Question(question="Identify error: She do not like coffee.", option1="She", option2="do", option3="not", option4="like",
         answer="do", category="verbal", topic="error", difficulty="medium"),

Question(question="Identify error: He go to school daily.", option1="He", option2="go", option3="to", option4="school",
         answer="go", category="verbal", topic="error", difficulty="easy"),
]

    db.session.add_all(questions)
    db.session.commit()

    print("✅ All questions added successfully!")