import streamlit as st
import datetime

st.set_page_config(
    page_title="微型 TimeTree",
    layout="wide"
)

# =========================
# 群組選擇
# =========================
mode = st.radio(
    "選擇群組",
    ["學生", "老師", "家長會", "校友會"],
    horizontal=True
)

# =========================
# 初始化 Session
# =========================
if "mylist" not in st.session_state:
    st.session_state.mylist = []

# =========================
# 左右欄位
# =========================
l, r = st.columns(2)

# =========================
# 左邊：新增行程
# =========================
with l:

    st.header("新增行程")

    t1 = st.text_input("行程主旨")

    t3 = st.date_input(
        "日期選擇",
        datetime.date.today()
    )

    t4 = st.time_input("時間選擇")

    n1 = st.number_input(
        "行程開始前幾分鐘提醒？",
        min_value=0,
        max_value=60,
        value=15
    )

    if st.button("新增行程"):

        # 改成 dictionary
        st.session_state.mylist.append({
            "title": t1,
            "date": t3,
            "time": t4,
            "remind": n1,
            "group": mode
        })

        st.success("新增成功")

# =========================
# 右邊：顯示行程
# =========================
with r:

    st.header("行程列表")

    if len(st.session_state.mylist) == 0:
        st.info("目前沒有行程")

    else:

        for item in st.session_state.mylist:

            # 卡片容器
            with st.container(border=True):

                st.subheader(f"📌 {item['title']}")

                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"📅 日期：{item['date']}")

                with col2:
                    st.write(f"⏰ 時間：{item['time']}")

                st.write(f"👥 群組：{item['group']}")

                st.write(
                    f"🔔 提前 {item['remind']} 分鐘提醒"
                )

                st.divider()
