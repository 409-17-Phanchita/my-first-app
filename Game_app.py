import time
import streamlit as st

st.title("🧪 เกมทายตารางธาตุ")
st.write("ทายชื่อธาตุจากสัญลักษณ์และเลขอะตอม")


# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""

if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""

if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""

if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""

if "start_time" not in st.session_state:
    st.session_state.start_time = None

if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "game_finished" not in st.session_state:
    st.session_state.game_finished = False

if "score" not in st.session_state:
    
# ฟังก์ชันเมื่อดล่นเกม

 def start_game():

    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.ans5_val = ""

    st.session_state.score = 0
    st.session_state.start_time = time.time()

    st.session_state.game_started = True
    st.session_state.game_finished = False

    st.rerun()



# ฟังก์ชันเริ่มเกมใหม่

def restart_game():

    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.ans5_val = ""

    st.session_state.score = 0
    st.session_state.start_time = None

    st.session_state.game_started = False
    st.session_state.game_finished = False

    st.rerun()



# ปุ่มเริ่มเกม / เริ่มใหม่

if not st.session_state.game_started:

    if not st.session_state.game_finished:

        if st.button("▶️ เริ่มเกม"):
           start_game()

    else:

        if st.button("🔄 เริ่มใหม่"):
            restart_game()



# เกม

if st.session_state.game_started and not st.session_state.game_finished:

    # คำนวณเวลาที่เหลือ
    elapsed_time = time.time() - st.session_state.start_time
    time_left = 45 - int(elapsed_time)

    if time_left > 0:

        st.error(f"⏳ เวลาที่เหลือ: {time_left} วินาที")

    else:

        st.warning("⏰ หมดเวลา!")

        # ตรวจคำตอบอัตโนมัติ
        u_ans1 = st.session_state.ans1_val.strip().lower()
        u_ans2 = st.session_state.ans2_val.strip().lower()
        u_ans3 = st.session_state.ans3_val.strip().lower()
        u_ans4 = st.session_state.ans4_val.strip().lower()
        u_ans5 = st.session_state.ans5_val.strip().lower()

        score = 0

        if u_ans1 in ["เบริลเลียม", "beryllium"]:
            score += 1

        if u_ans2 in ["เจอร์เมเนียม", "germanium"]:
            score += 1

        if u_ans3 in ["ยูโรเพียม", "europium"]:
            score += 1

        if u_ans4 in ["ทังสเตน", "tungsten"]:
            score += 1

        if u_ans5 in ["เฟอร์เมียม", "fermium"]:
            score += 1

        st.session_state.score = score
        st.session_state.game_finished = True

        st.rerun()


    
    # ข้อ 1
    

    st.subheader("ข้อ 1")
    st.write("สัญลักษณ์ **Be** เลขอะตอม **4** คือธาตุอะไร?")

    ans1 = st.text_input(
        "คำตอบข้อ 1",
        value=st.session_state.ans1_val
    )

    st.session_state.ans1_val = ans1


    # ข้อ 2
    

    st.subheader("ข้อ 2")
    st.write("สัญลักษณ์ **Ge** เลขอะตอม **32** คือธาตุอะไร?")

    ans2 = st.text_input(
        "คำตอบข้อ 2",
        value=st.session_state.ans2_val
    )

    st.session_state.ans2_val = ans2


    # ข้อ 3

    st.subheader("ข้อ 3")
    st.write("สัญลักษณ์ **Eu** เลขอะตอม **63** คือธาตุอะไร?")

    ans3 = st.text_input(
        "คำตอบข้อ 3",
        value=st.session_state.ans3_val
    )

    st.session_state.ans3_val = ans3

  
    # ข้อ 4
  
    st.subheader("ข้อ 4")
    st.write("สัญลักษณ์ **W** เลขอะตอม **74** คือธาตุอะไร?")

    ans4 = st.text_input(
        "คำตอบข้อ 4",
        value=st.session_state.ans4_val
    )

    st.session_state.ans4_val = ans4


    # ข้อ 5

    st.subheader("ข้อ 5")
    st.write("สัญลักษณ์ **Fm** เลขอะตอม **100** คือธาตุอะไร?")

    ans5 = st.text_input(
        "คำตอบข้อ 5",
        value=st.session_state.ans5_val
    )

    st.session_state.ans5_val = ans5


    st.write("---")


    # ปุ่มตรวจคำตอบ

    if st.button("✅ ตรวจคำตอบ"):

        # แปลงคำตอบให้เป็นตัวพิมพ์เล็กและตัดช่องว่าง
        u_ans1 = ans1.strip().lower()
        u_ans2 = ans2.strip().lower()
        u_ans3 = ans3.strip().lower()
        u_ans4 = ans4.strip().lower()
        u_ans5 = ans5.strip().lower()

        score = 0

        # ตรวจคำตอบ
        if u_ans1 in ["เบริลเลียม", "beryllium"]:
            score += 1

        if u_ans2 in ["เจอร์เมเนียม", "germanium"]:
            score += 1

        if u_ans3 in ["ยูโรเพียม", "europium"]:
            score += 1

        if u_ans4 in ["ทังสเตน", "tungsten"]:
            score += 1

        if u_ans5 in ["เฟอร์เมียม", "fermium"]:
            score += 1

        st.session_state.score = score
        st.session_state.game_finished = True

        st.rerun()


# แสดงผลเมื่อจบเกม

if st.session_state.game_finished:

    score = st.session_state.score

    st.write("---")

    st.write(f"### คะแนนของคุณ: {score} / 5")


    # เกณฑ์ประเมินผู้เล่น

    if score == 5:

        st.success(
            "อย่างโหดเลยคร้าบจารย์! ตอบถูกทั้ง 5 ข้อ"
        )

    elif score == 4:

        st.info(
            "So Very Good but พยายามอีกนิสส์"
        )

    elif score == 3:

        st.info(
            "พี่ทำได้มากกว่านี้แน่นอน!"
        )

    elif score == 2:

        st.warning(
            "พยายามกว่านี้นะะ"
        )

    elif score == 1:

        st.warning(
            "สู้ๆละคนดีของพี่"
        )

    elif score == 0:

        st.warning(
            "พยายามอีกนิสนะน้อง💪🏻"
        )

    
    # แสดงเฉลย


    st.write("### 📖 เฉลย")

    st.write("1. Be = เบริลเลียม (Beryllium)")
    st.write("2. Ge = เจอร์เมเนียม (Germanium)")
    st.write("3. Eu = ยูโรเพียม (Europium)")
    st.write("4. W = ทังสเตน (Tungsten)")
    st.write("5. Fm = เฟอร์เมียม (Fermium)")

    
    # ปุ่มเริ่มใหม่หลังจบเกม

    if st.button("🔄 เริ่มใหม่"):
        restart_game()
