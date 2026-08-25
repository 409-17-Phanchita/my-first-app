import time
import streamlit as st

st.title("⏱️ เกมเติมคำศัพท์จับเวลา")

# =====================================================
# จุดที่ 1 : กำหนดค่าเริ่มต้นใน session_state
# =====================================================

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


# =====================================================
# จุดที่ 2 : ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
# =====================================================

def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""

    st.session_state.start = time.time()
    st.session_state.is_ended = False


# =====================================================
# ฟังก์ชัน MessageBox (Dialog)
# =====================================================

@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):

    st.balloons()

    score = 0

    # จุดที่ 3 : สรุปผลการเล่น
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    # ตรวจข้อ 1
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error("❌ ข้อ 1: ยังไม่ถูกต้อง")

    # ตรวจข้อ 2
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error("❌ ข้อ 2: ยังไม่ถูกต้อง")

    # จุดที่ 4 : ตรวจข้อ 3
    if u_ans3 == "peach":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error("❌ ข้อ 3: ยังไม่ถูกต้อง")

    # ตรวจข้อ 4
    if u_ans4 == "balloon":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error("❌ ข้อ 4: ยังไม่ถูกต้อง")

    # จุดที่ 5 : คะแนนเต็ม 4
    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# =====================================================
# ปุ่มเริ่มเล่นเกม
# =====================================================

st.button(
    "🎮 เริ่มเล่นเกม",
    on_click=reset_game
)


# =====================================================
# แสดงเวลานับถอยหลัง
# =====================================================

if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    time_left = int(
        30 - (time.time() - st.session_state.start)
    )

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()


st.divider()


# =====================================================
# จุดที่ 6 : ช่องรับคำตอบ
# =====================================================

ans1 = st.text_input(
    "ข้อ 1: An a__le a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val
)

ans2 = st.text_input(
    "ข้อ 2: Cats love to eat f__h. 🐟",
    value=st.session_state.ans2_val
)

ans3 = st.text_input(
    "ข้อ 3: I like to eat a pe__h. 🍑",
    value=st.session_state.ans3_val
)

ans4 = st.text_input(
    "ข้อ 4: The ba__oon is flying in the sky. 🎈",
    value=st.session_state.ans4_val
)


# =====================================================
# จุดที่ 7 : อัปเดตค่าล่าสุดเข้าตัวแปร
# =====================================================

st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4


# =====================================================
# จุดที่ 4 : ปุ่มส่งคำตอบ
# =====================================================

if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    if st.button("📤 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()


# =====================================================
# จุดที่ 8 : แสดง Dialog ผลลัพธ์
# =====================================================

if st.session_state.is_ended:

    show_result_dialog(
        st.session_state.ans1_val,
        st.session_state.ans2_val,
        st.session_state.ans3_val,
        st.session_state.ans4_val
    )


st.divider()

st.write("🍎 Apple")
st.write("🐟 Fish")
st.write("🍑 Peach")
st.write("🎈 Balloon")

st.write("นางสาวพัณณ์ชิตา จองทุน เลขที่ 17 ม.4/9")
