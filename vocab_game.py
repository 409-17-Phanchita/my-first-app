import time
import streamlit as st

st.title("⏱️ เกมเติมคำศัพท์จับเวลา")

# จุดที่ 1 : กำหนดค่าเริ่มต้น
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""

if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""

if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""

if "start" not in st.session_state:
    st.session_state.start = None

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False


# จุดที่ 2 : ฟังก์ชันเริ่มเกมใหม่
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""

    st.session_state.start = time.time()
    st.session_state.is_ended = False


# จุดที่ 3 : แสดงผลคะแนน
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):

    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    # ตรวจข้อ 1
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # จุดที่ 4 : ตรวจข้อ 3
    if u_ans3 == "peach":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    # ตรวจข้อ 4
    if u_ans4 == "balloon":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    # จุดที่ 5 : คะแนนเต็ม 4
    st.info(f"🏆 ได้คะแนนรวม: {score} / 4 คะแนน")

    if score == 4:
        st.success("🎉 You win! ตอบถูกครบทั้ง 4 ข้อ")
    else:
        st.error("💀 You lose! ลองใหม่อีกครั้งนะ")


# ปุ่มเริ่มเกม
st.button(
    "🎮 เริ่มเล่นเกม",
    on_click=reset_game
)


# แสดงเวลานับถอยหลัง
if st.session_state.start is not None and not st.session_state.is_ended:

    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.warning(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()


st.divider()


# จุดที่ 6 : ช่องรับคำตอบ 4 ข้อ

ans1 = st.text_input(
    "ข้อ 1: An apple a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val
)

ans2 = st.text_input(
    "ข้อ 2: Cats love to eat fish. 🐟",
    value=st.session_state.ans2_val
)

ans3 = st.text_input(
    "ข้อ 3: I like to eat a ______. 🍑",
    value=st.session_state.ans3_val
)

ans4 = st.text_input(
    "ข้อ 4: The ______ is flying in the sky. 🎈",
    value=st.session_state.ans4_val
)


# จุดที่ 7 : อัปเดตค่าล่าสุด
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4


# ปุ่มส่งคำตอบ
if st.session_state.start is not None and not st.session_state.is_ended:

    if st.button("📤 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()


# จุดที่ 8 : แสดง Dialog ผลลัพธ์
if st.session_state.is_ended:

    if st.session_state.start is not None:
        show_result_dialog(
            st.session_state.ans1_val,
            st.session_state.ans2_val,
            st.session_state.ans3_val,
            st.session_state.ans4_val
        )


st.divider()

st.write("🌟 คำศัพท์ในเกม")
st.write("1. Apple = แอปเปิล 🍎")
st.write("2. Fish = ปลา 🐟")
st.write("3. Peach = ลูกพีช 🍑")
st.write("4. Balloon = ลูกโป่ง 🎈")

st.divider()
st.write("นางสาวพัณณ์ชิตา จองทุน เลขที่ 17 ม.4/9")
