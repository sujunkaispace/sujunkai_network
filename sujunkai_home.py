'''我的主页'''
import streamlit as st
from PIL import Image,ImageOps
import SparkApi
import time

appid = "d303d929"     #填写控制台中获取的 APPID 信息
api_secret = "NjNjNTJkZGFmMTQyZWQzYzVlNDFkNWU1"   #填写控制台中获取的 APISecret 信息
api_key ="63db2a6a11da05a18dd826e4c0365b37"    #填写控制台中获取的 APIKey 信息
domain = "general"   # v1.5版本
Spark_url = "ws://spark-api.xf-yun.com/v1.1/chat"  # v1.5环境的地址

page = st.sidebar.radio("我的首页",["我的兴趣推荐","我的图片处理工具","我的智慧词典","我的留言区","我的智能助手"])

def progress_bar(loading_message='正在加载',loading_time=0.01):
    loading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(loading_time)
        loading.progress(i,loading_message+str(i)+'%')
    loading.progress(100, '加载完毕！')
    loading.empty()

def img_change(img, rc=0, gc=1, bc=2):
    # 处理过程
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

def page1():
    st.title("我的兴趣推荐页")
    st.write("我的爱好有编程,我在编程创赛营做了一些编程作品：")
    st.image("sujunkai_踩砖块.gif")
    st.write("----")
    st.write("我也很喜欢听相声，这是我最爱听的其中之一:《爆竹声中一岁除》")
    st.video("sujunkai_相声：《爆竹声中一岁除》.mp4")
    st.write("----")
    st.write("我还很喜欢游泳，这是我去关于游泳的一些视频")
    col1,col2 = st.columns([1,1])
    with col1:
        cb3 = st.video("sujunkai_swimming.mp4")
    with col2:
        cb4 = st.video("sujunkai_diving.mp4")
    st.write("----")
    st.write("我也学习过书法，这是我练习书法时的一些照片")
    st.image("sujunkai_calligraphy.jpg")
    # st.audio("")
    # st.video("")
def page2():
    st.title(":sunglasses:我的图片处理工具:sunglasses:")
    uploaded_file = st.file_uploader("上传文件",type=["png","jpg","jpeg"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        change1, change2 = st.tabs(["图片改色","颜色反转"])
        with change1:
            c1_tab1, c1_tab2, c1_tab3, c1_tab4 = st.tabs(["原图", "改色1", "改色2","改色3"])
            with c1_tab1:
                st.image(img)
            with c1_tab2:
                progress_bar()
                st.image(img_change(img, 0, 2, 1))
            img = Image.open(uploaded_file)
            with c1_tab3:
                progress_bar()
                st.image(img_change(img, 2, 1, 0))
            img = Image.open(uploaded_file)
            with c1_tab4:
                progress_bar()
                st.image(img_change(img, 1, 0, 2))
            img = Image.open(uploaded_file)
        with change2:
            c2_tab1, c2_tab2 = st.tabs(["原图", "反色后"])
            with c2_tab1:
                st.image(img)
            with c2_tab2:
                progress_bar()
                st.image(ImageOps.invert(img))
            img = Image.open(uploaded_file)
            
def page3():
    st.title("智慧词典")
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split("#")
    # 读取次数文档，用\n切割成列表
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")

    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]

    word = st.text_input("请输入要查询的单词")
    st.write("----")
    if word in words_dict:
        st.write(word+"的中文是：")
        st.write(words_dict[word][1])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        st.write("查询次数：", times_dict[n])
        if word == 'python':
            st.code('''
                    #恭喜你，触发彩蛋
                    print("I love Python~")
                    ''')
            st.balloons()
        if word == 'school' or word == 'homework':
            st.snow()
        if word == 'jocker':
            st.image("sujunkai_jocker.png")
            st.audio("sujunkai_jocker_音效.ogg")
        with open("check_out_times.txt", "w") as f:
            message = ""
            for k,v in times_dict.items():
                message += str(k) + "#" + str(v) + "\n"
            message = message[:-1]
            f.write(message)

def page4():
    st.title("留言板")
    st.write("如果没有显示你留言的内容，可以尝试刷新一下")
    with open("leave_messages.txt","r",encoding="utf-8") as f:
        messages_list = f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
        
    for i in messages_list:
        if i[1] == '苏俊恺':
            with st.chat_message('😎'):
                st.write(i[1], ":", i[2])
        else:
            with st.chat_message('😎'):
                st.write(i[1], ":", i[2])
    st.write("----")
    st.write("你的名字：")
    name_choose1,name_choose2 = st.tabs(["选择名字","自己输入"])
    with name_choose1:
        name_1 = st.selectbox('我是……', ["苏俊恺", "李鑫宇", "黄凯跃"])
    with name_choose2:
        name_2 = st.text_input("请输入你的名字")
    if name_2 != "":
        name = name_2
    else:
        name = name_1
    new_message = st.text_input("想要说的话……")
    if st.button("留言"):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open("leave_messages.txt", "w", encoding="utf-8") as f:
            message = ""
            for i in messages_list:
                 message += i[0] + "#" + i[1] + "#" + i[2] + "\n"
            message = message[:-1]
            f.write(message)
                
def page5():
    st.title("智能助手")
    Input = st.text_input("请输入你的问题")
    answer = SparkApi.main(appid, api_key, api_secret, Spark_url, domain, Input)
    st.write("----")
    st.write("智能助手:")
    st.write(answer)

if page=="我的兴趣推荐":
    page1()
elif page=="我的图片处理工具":
    page2()
elif page=="我的智慧词典":
    page3()
elif page=="我的留言区":
    page4()
elif page=="我的智能助手":
    page5()
