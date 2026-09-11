# --------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# --------------------------------------------------

st.dialog("📋 สรุปผลการเล่นเกม")
def show_result_dialog():

    st.balloons()

    score = 0

    u_ans1 = st.session_state.ans1_val.strip().lower()
    u_ans2 = st.session_state.ans2_val.strip().lower()
    u_ans3 = st.session_state.ans3_val.strip().lower()
    u_ans4 = st.session_state.ans4_val.strip().lower()
    u_ans5 = st.session_state.ans5_val.strip().lower()

    # --------------------------------------------------
    # ตรวจคำตอบ
    # --------------------------------------------------

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


    # --------------------------------------------------
    # แสดงคะแนนรวม
    # --------------------------------------------------

    st.info(f"🏆 ได้คะแนนรวม: {score} / 5 คะแนน")


    # --------------------------------------------------
    # 📊 เกณฑ์ประเมินผู้เล่น
    # --------------------------------------------------

    st.write("### 📊 เกณฑ์ประเมินผู้เล่น")

    if score == 5:

        st.success(
            "🌟 อย่างโหดเลยคร้าบจารย์! ตอบถูกทั้ง 5 ข้อ"
        )

    elif score == 4:

        st.info(
            "👍 So Very Good but พยายามอีกนิสส์"
        )

    elif score == 3:

        st.info(
            "💪 พี่ทำได้มากกว่านี้แน่นอน!"
        )

    elif score == 2:

        st.warning(
            "✌️ พยายามกว่านี้นะะ"
        )

    elif score == 1:

        st.warning(
            "❤️ สู้ๆละคนดีของพี่"
        )

    else:

        st.error(
            "💪🏻 พยายามอีกนิสนะน้อง💪🏻"
        )


    # --------------------------------------------------
    # 📖 เฉลย
    # --------------------------------------------------

    st.write("### 📖 เฉลย")

    st.write("1. Be = เบริลเลียม (Beryllium)")
    st.write("2. Ge = เจอร์เมเนียม (Germanium)")
    st.write("3. Eu = ยูโรเพียม (Europium)")
    st.write("4. W = ทังสเตน (Tungsten)")
    st.write("5. Fm = เฟอร์เมียม (Fermium)")
