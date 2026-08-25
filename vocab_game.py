import time
import streamlit as st

st.title("⏱️ เกมเติมคำศัพท์จับเวลา")


# =========================================================
# จุดที่ 1 : เพิ่มการกำหนดค่าเริ่มต้นใน session_state
# =========================================================

if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""

if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

# เพิ่มข้อ 3
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""

# เพิ่มข้อ 4
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""


# =========================================================
# ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
# =========================================================

def reset_game():

    # จุดที่ 2 : เพิ่มการเคลียร์ค่าข้อ 3 และข้อ 4
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""

    st.session_state.start = time.time()
    st.session_state.is_ended = False


# =========================================================
# ฟังก์ชัน MessageBox (Dialog)
# =========================================================

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
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")


    # ตรวจข้อ 2
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")


    # จุดที่ 4 : เพิ่มการตรวจข้อ 3 และข้อ 4

    # ตรวจข้อ 3
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


    # จุดที่ 5 : เปลี่ยนคะแนนเต็มเป็น 4
    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# =========================================================
# 1. ปุ่มเริ่มเล่นเกม
# =========================================================

st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)


# =========================================================
# 2. แถบแสดงเวลานับถอยหลัง
# =========================================================

if "start" in st.session_state and not st.session_state.get("is_ended", False):

    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()


st.divider()


# =========================================================
# จุดที่ 6 : เพิ่มช่องรับคำตอบ ans3 และ ans4
# =========================================================

ans1 = st.text_input(
    "ข้อ 1: An a__le a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val
)

ans2 = st.text_input(
    "ข้อ 2: Cats love to eat f__h. 🐟",
    value=st.session_state.ans2_val
)

# ข้อ 3 : Peach
ans3 = st.text_input(
    "ข้อ 3: I like to eat a pe__h. 🍑",
    value=st.session_state.ans3_val
)

# ข้อ 4 : Balloon
ans4 = st.text_input(
    "ข้อ 4: The ba__oon is flying in the sky. 🎈",
    value=st.session_state.ans4_val
)


# =========================================================
# จุดที่ 7 : อัปเดตค่าล่าสุดเข้าตัวแปร
# =========================================================

st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4


# =========================================================
# จุดที่ 4 : ปุ่มส่งคำตอบ
# =========================================================

if "start" in st.session_state and not st.session_state.get("is_ended", False):

    if st.button("📤 ส่งคำตอบ"):

        st.session_state.is_ended = True
        st.rerun()


# =========================================================
# จุดที่ 8 : แสดง Dialog ผลลัพธ์
# =========================================================

if st.session_state.get("is_ended", False):

    show_result_dialog(
        st.session_state.ans1_val,
        st.session_state.ans2_val,
        st.session_state.ans3_val,
        st.session_state.ans4_val
    )


# =========================================================
# แสดงคำศัพท์
# =========================================================

st.divider()

st.write("🍎 Apple = แอปเปิล")
st.write("🐟 Fish = ปลา")
st.write("🍑 Peach = ลูกพีช")
st.write("🎈 Balloon = ลูกโป่ง")

st.write("นางสาวพัณณ์ชิตา จองทุน เลขที่ 17 ม.4/9")
