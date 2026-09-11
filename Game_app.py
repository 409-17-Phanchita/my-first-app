import time
import streamlit as st

st.title("🧪 เกมทายตารางธาตุ")
st.write("ทายชื่อธาตุจากสัญลักษณ์และเลขอะตอม")

# --------------------------------------------------
# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
# --------------------------------------------------

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

if "start" not in st.session_state:
    st.session_state.start = None

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False

if "current_q" not in st.session_state:
    st.session_state.current_q = 1


# --------------------------------------------------
# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
# --------------------------------------------------

def reset_game():

    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.ans5_val = ""

    st.session_state.current_q = 1

    st.session_state.start = time.time()

    st.session_state.is_ended = False

    st.rerun()


# --------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# --------------------------------------------------

@st.dialog("📋 สรุปผลการเล่นเกม")
def show_result_dialog():

    st.balloons()

    score = 0

    u_ans1 = st.session_state.ans1_val.strip().lower()
    u_ans2 = st.session_state.ans2_val.strip().lower()
    u_ans3 = st.session_state.ans3_val.strip().lower()
    u_ans4 = st.session_state.ans4_val.strip().lower()
    u_ans5 = st.session_state.ans5_val.strip().lower()

    # ตรวจข้อ 1
    if u_ans1 in ["เบริลเลียม", "beryllium"]:
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 in ["เจอร์เมเนียม", "germanium"]:
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # ตรวจข้อ 3
    if u_ans3 in ["ยูโรเพียม", "europium"]:
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    # ตรวจข้อ 4
    if u_ans4 in ["ทังสเตน", "tungsten"]:
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    # ตรวจข้อ 5
    if u_ans5 in ["เฟอร์เมียม", "fermium"]:
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")

    # แสดงคะแนนรวม
    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 5:
        st.success("🎉 อย่าโหดคร้าบจารย์! ตอบถูกทั้งหมด 5 ข้อ")
    elif score >= 3:
        st.info("👍 So Very Good but พยายามอีกนิสส์")
    else:
        st.warning("ลองทบทวนตารางธาตุแล้วเล่นใหม่อีกครั้ง")


# --------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# --------------------------------------------------

st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)


# --------------------------------------------------
# 2. แสดงเวลานับถอยหลัง
# --------------------------------------------------

if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    time_left = int(
        30 - (time.time() - st.session_state.start)
    )

    if time_left > 0:

        st.error(
            f"⏳ เหลือเวลา: {time_left} วินาที"
        )

    else:

        # หมดเวลา
        st.warning(
            f"⏰ หมดเวลา ข้อ {st.session_state.current_q}!"
        )

        # ถ้ายังไม่ถึงข้อสุดท้าย
        if st.session_state.current_q < 5:

            st.session_state.current_q += 1

            # เริ่มเวลาใหม่ 30 วินาที
            st.session_state.start = time.time()

            time.sleep(1)

            st.rerun()

        else:

            # หมดเวลาในข้อสุดท้าย
            st.session_state.is_ended = True

            st.rerun()


st.divider()


# --------------------------------------------------
# 3. ช่องรับคำตอบ
# --------------------------------------------------

if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    # --------------------------------------------------
    # ข้อ 1
    # --------------------------------------------------

    if st.session_state.current_q == 1:

        st.subheader("ข้อ 1")

        st.write(
            "สัญลักษณ์ **Be** เลขอะตอม **4** "
            "คือธาตุอะไร?"
        )

        ans1 = st.text_input(
            "คำตอบข้อ 1",
            value=st.session_state.ans1_val,
        )

        st.session_state.ans1_val = ans1


    # --------------------------------------------------
    # ข้อ 2
    # --------------------------------------------------

    elif st.session_state.current_q == 2:

        st.subheader("ข้อ 2")

        st.write(
            "สัญลักษณ์ **Ge** เลขอะตอม **32** "
            "คือธาตุอะไร?"
        )

        ans2 = st.text_input(
            "คำตอบข้อ 2",
            value=st.session_state.ans2_val,
        )

        st.session_state.ans2_val = ans2


    # --------------------------------------------------
    # ข้อ 3
    # --------------------------------------------------

    elif st.session_state.current_q == 3:

        st.subheader("ข้อ 3")

        st.write(
            "สัญลักษณ์ **Eu** เลขอะตอม **63** "
            "คือธาตุอะไร?"
        )

        ans3 = st.text_input(
            "คำตอบข้อ 3",
            value=st.session_state.ans3_val,
        )

        st.session_state.ans3_val = ans3


    # --------------------------------------------------
    # ข้อ 4
    # --------------------------------------------------

    elif st.session_state.current_q == 4:

        st.subheader("ข้อ 4")

        st.write(
            "สัญลักษณ์ **W** เลขอะตอม **74** "
            "คือธาตุอะไร?"
        )

        ans4 = st.text_input(
            "คำตอบข้อ 4",
            value=st.session_state.ans4_val,
        )

        st.session_state.ans4_val = ans4


    # --------------------------------------------------
    # ข้อ 5
    # --------------------------------------------------

    elif st.session_state.current_q == 5:

        st.subheader("ข้อ 5")

        st.write(
            "สัญลักษณ์ **Fm** เลขอะตอม **100** "
            "คือธาตุอะไร?"
        )

        ans5 = st.text_input(
            "คำตอบข้อ 5",
            value=st.session_state.ans5_val,
        )

        st.session_state.ans5_val = ans5


    # --------------------------------------------------
    # 4. ปุ่มส่งคำตอบ
    # --------------------------------------------------

    if st.button("📩 ส่งคำตอบ"):

        # ถ้ายังไม่ถึงข้อสุดท้าย
        if st.session_state.current_q < 5:

            st.session_state.current_q += 1

            # เริ่มเวลาใหม่ 30 วินาที
            st.session_state.start = time.time()

            st.rerun()

        else:

            # ส่งข้อสุดท้ายแล้วจบเกม
            st.session_state.is_ended = True

            st.rerun()


# --------------------------------------------------
# 5. แสดง Dialog ผลลัพธ์
# --------------------------------------------------

if st.session_state.is_ended:

    show_result_dialog()
