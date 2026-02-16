import streamlit as st
import base64

st.set_page_config(page_title="祝女王生日快乐", layout="centered")

# 1. 确保视频文件名正确
video_file = "1.mp4" 

def get_base64_video(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

try:
    video_base64 = get_base64_video(video_file)

    # 这里的 CSS 增加了 animation 动画
    # 'move-up' 动画会让文字在第 3.5 秒后才开始向上移动
    st.markdown(f"""
        <style>
        .video-container {{
            position: relative;
            width: 100%;
            background-color: black;
        }}
        .overlay-text {{
            position: absolute;
            bottom: -100px; /* 初始位置在视频下方不可见处 */
            left: 50%;
            transform: translateX(-50%);
            color: gold;
            text-align: center;
            z-index: 10;
            width: 80%;
            pointer-events: none;
            text-shadow: 2px 2px 4px #000000;
            
            /* 动画设置：延迟 3.5 秒开始，持续 4 秒，保持在终点状态 */
            animation: move-up 4s ease-out 3.5s forwards;
        }}
        
        @keyframes move-up {{
            from {{ bottom: -100px; opacity: 0; }}
            to {{ bottom: 30%; opacity: 1; }}
        }}
        </style>
        
        <div class="video-container">
            <video width="100%" autoplay controls>
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            </video>
            <div class="overlay-text">
                <h2 style="font-size: 36px; margin-bottom: 5px;">致我心中永远的女王</h2>
                <p style="font-size: 18px; color: white; margin: 2px;">姓冠“王”者，天生风范</p>
                <p style="font-size: 18px; color: white; margin: 2px;">命属“马”者，志在千里</p>
                <h3 style="color: red; font-size: 28px; margin-top: 10px;">生日快乐，我的女王！</h3>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.write("") # 留点间距
    if st.button("再次触发满天祝福"):
        st.balloons()
        st.snow()

except FileNotFoundError:
    st.error("请确保视频文件名正确。")