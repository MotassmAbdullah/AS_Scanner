import numpy as np
import pandas as pd
import streamlit as st
import cv2


# import scipy.interpolate
def ASS(im, d, o):
    cont = []
    re = []

    if o == "Vertical":
        sh = int((d[3] - d[2]) / d[4])
        se = int(d[2])
        for t in range(d[4]):
            # st.image(im[int(d[0]):int(d[1]), se:se + sh])
            c_sh = int((d[1] - d[0]) / d[5])
            c_se = int(d[0])
            for y in range(d[5]):
                cont.append(np.average(im[c_se:c_se + c_sh, se:se + sh]))
                c_se = c_se + c_sh
            re.append(cont.index(min(cont)))
            cont = []
            se = se + sh
    elif o == "Horizontal":
        sh = int((d[1] - d[0]) / d[4])
        se = int(d[0])
        for t in range(d[4]):
            # st.image(im[se:se + sh, d[2]:d[3]])
            c_sh = int((d[3] - d[2]) / d[5])
            c_se = int(d[2])
            for y in range(d[5]):
                cont.append(np.average(im[se:se + sh, c_se:c_se + c_sh]))
                c_se = c_se + c_sh
            re.append((cont.index(min(cont))))
            cont = []
            se = se + sh
    else:
        st.error("Some data missing R04")
    if re is None:
        st.error("no result")
    else:
        # st.write("".join(str(e) for e in re))
        return "".join(str(e) for e in re)


if __name__ == '__main__':
    st.set_page_config("AS Scanner", ":scroll:")
    st.sidebar.progress(3, "Memberships ( 2,000,000 $$)  عداد المشتركين")
    st.title("AS Scanner قارئ اوراق الاجابات")
    st.sidebar.info('License expiry date 1/1/2024 نهاية الاشتراك')
    st.sidebar.info("0.1.0 (Privet app تطبيق خاص)")
    st.sidebar.success("Contact +966503029722 للتواصل")
    if "page" not in st.session_state:
        st.session_state.page = 0
        st.session_state.img = cv2.imread("./img_1.jfif")
        st.session_state.sup = None
        st.balloons()

    if st.session_state.page == 0:
        st.subheader("Welcome Moaiad أهلا مؤيد")
        if st.session_state.sup is None:
            st.session_state.input_im = st.radio("Input", ["Example نموذج", "Solved Ex نموذج محلول", "Upload ارفع الملف"], 1)
        else:
            st.session_state.input_im = st.radio("Input", ["Example نموذج", "Solved Ex نموذج محلول", "Upload ارفع الملف"], st.session_state.sup)
        st.text("<<<Preview image in the side bar إستعرض الورقة في الشريط الجانبي<<<")
        st.sidebar.title("Preview إستعراض")
        if st.session_state.input_im == "Example نموذج" and st.session_state.sup is None:
            st.session_state.img = cv2.imread("./img_1.jfif", cv2.IMREAD_GRAYSCALE)
            st.session_state.data = [[152, (192 + 152), 368, (190 + 368), 10, 10],
                                     [152, (192 + 152), 260, (99 + 260), 5, 10],
                                     [152, (192 + 152), 209, (40 + 209), 2, 10],
                                     [380, (52 + 380), 540, (17 + 540), 1, 3],
                                     [380, (52 + 380), 477, (17 + 477), 1, 2],
                                     [380, (52 + 380), 380, (17 + 380), 1, 3],
                                     [373, (52 + 373), 347, (17 + 347), 1, 3],
                                     [380, (52 + 380), 292, (17 + 292), 1, 2],
                                     [373, (52 + 373), 252, (17 + 252), 1, 2],
                                     [525, (290 + 525), 444, (90 + 444), 15, 4],
                                     [525, (290 + 525), 315, (90 + 315), 15, 4],
                                     [525, (290 + 525), 187, (90 + 187), 15, 4],
                                     [525, (290 + 525), 56, (90 + 56), 15, 4]]
            st.session_state.Orin = ["Vertical", "Vertical", "Vertical", "Vertical", "Vertical", "Vertical",
                                     "Vertical", "Vertical", "Vertical", "Horizontal", "Horizontal", "Horizontal",
                                     "Horizontal"]
            st.session_state.Field = ["National ID", "School ID", "Administration ID", "Course", "Student Grade",
                                      "Form", "School type",
                                      "Sex", "Nationality", "Answers 1", "Answers 2", "Answers 3", "Answers 4"]
        elif st.session_state.input_im == "Solved Ex نموذج محلول" and st.session_state.sup is None:
            st.session_state.img = cv2.imread("./img_2.jpg", cv2.IMREAD_GRAYSCALE)
            st.session_state.data = [[152, (192 + 152), 368, (190 + 368), 10, 10],
                                     [152, (192 + 152), 260, (99 + 260), 5, 10],
                                     [152, (192 + 152), 209, (40 + 209), 2, 10],
                                     [380, (52 + 380), 540, (17 + 540), 1, 3],
                                     [380, (52 + 380), 477, (17 + 477), 1, 2],
                                     [380, (52 + 380), 380, (17 + 380), 1, 3],
                                     [373, (52 + 373), 347, (17 + 347), 1, 3],
                                     [380, (52 + 380), 292, (17 + 292), 1, 2],
                                     [373, (52 + 373), 252, (17 + 252), 1, 2],
                                     [525, (290 + 525), 444, (90 + 444), 15, 4],
                                     [525, (290 + 525), 315, (90 + 315), 15, 4],
                                     [525, (290 + 525), 187, (90 + 187), 15, 4],
                                     [525, (290 + 525), 56, (90 + 56), 15, 4]]
            # st.session_state.ID_crop = [152, (192 + 152), 368, (190 + 368), 10, 10]
            # [ X , X + H , Y , Y + W , AC , AO]
            st.session_state.Orin = ["Vertical", "Vertical", "Vertical", "Vertical", "Vertical", "Vertical",
                                     "Vertical", "Vertical", "Vertical", "Horizontal", "Horizontal", "Horizontal",
                                     "Horizontal"]
            st.session_state.Field = ["National ID", "School ID", "Administration ID", "Course", "Student Grade",
                                      "Form", "School type", "Sex", "Nationality", "Answers 1", "Answers 2",
                                      "Answers 3", "Answers 4"]
        elif st.session_state.input_im == "Upload ارفع الملف" and st.session_state.sup is None:
            file_up = st.file_uploader("Upload your image إرفع الصورة هنا", accept_multiple_files=False)
            if file_up is not None:
                st.session_state.img = cv2.imdecode(np.fromstring(file_up.getvalue(), np.uint8), cv2.IMREAD_GRAYSCALE)
            else:
                st.error("No Images uploaded تأكد من الملف المرفوع")
                with st.spinner():
                    st.stop()
            st.info("Make sure scanning areas are correct تأكد من تحديد مناطق الاحل")
            st.session_state.Orin = ["Vertical", "Vertical", "Vertical", "Vertical", "Vertical", "Vertical",
                                     "Vertical", "Vertical", "Vertical", "Horizontal", "Horizontal", "Horizontal",
                                     "Horizontal"]
            st.session_state.Field = ["National ID", "School ID", "Administration ID", "Course", "Student Grade",
                                      "Form", "School type", "Sex", "Nationality", "Answers 1", "Answers 2",
                                      "Answers 3", "Answers 4"]
            st.session_state.data = [[152, (192 + 152), 368, (190 + 368), 10, 10],
                                     [152, (192 + 152), 260, (99 + 260), 5, 10],
                                     [152, (192 + 152), 209, (40 + 209), 2, 10],
                                     [380, (52 + 380), 540, (17 + 540), 1, 3],
                                     [380, (52 + 380), 477, (17 + 477), 1, 2],
                                     [380, (52 + 380), 380, (17 + 380), 1, 3],
                                     [373, (52 + 373), 347, (17 + 347), 1, 3],
                                     [380, (52 + 380), 292, (17 + 292), 1, 2],
                                     [373, (52 + 373), 252, (17 + 252), 1, 2],
                                     [525, (290 + 525), 444, (90 + 444), 15, 4],
                                     [525, (290 + 525), 315, (90 + 315), 15, 4],
                                     [525, (290 + 525), 187, (90 + 187), 15, 4],
                                     [525, (290 + 525), 56, (90 + 56), 15, 4]]
        st.sidebar.image(st.session_state.img, st.session_state.input_im)
        L1, L3 = st.columns(2)
        with L1:
            if st.button("Scanning area حدد مناطق الحل", type="secondary", use_container_width=True):
                st.session_state.page = 1
                st._rerun()
            # st.write(len(st.session_state.data))
            start = st.button("Start scanning استخرج النتائج", type="primary", use_container_width=True)
            if start:
                # img_crop = st.session_state.img[10:d[2], d[3]:d[4]]
                prog = st.progress(0, text='Please wait!! إنتظر رجاءً')
                T = [[]]
                for r in range(len(st.session_state.data)):  # [0]:#
                    prog.progress(int(200 / (len(st.session_state.data) - r + 1)))
                    if r < 3:
                        T[0].append(ASS(st.session_state.img, st.session_state.data[r], st.session_state.Orin[r]))
                    elif r == 3:
                        re = ASS(st.session_state.img, st.session_state.data[r], st.session_state.Orin[r])
                        if re == '0':
                            T[0].append("Language-لغتي")
                        elif re == '1':
                            T[0].append("Math-رياضيات")
                        elif re == '2':
                            T[0].append("Science-علوم")
                    elif r == 4:
                        re = ASS(st.session_state.img, st.session_state.data[r], st.session_state.Orin[r])
                        if re == '0':
                            T[0].append("6th Primary-سادس إبتدائي")
                        elif re == '1':
                            T[0].append("3th Intermediate-ثالث متوسط")
                    elif r == 5:
                        re = ASS(st.session_state.img, st.session_state.data[r], st.session_state.Orin[r])
                        if re == '0':
                            T[0].append("A-أ")
                        elif re == '1':
                            T[0].append("B-ب")
                        elif re == '2':
                            T[0].append("C-ج")
                    elif r == 6:
                        re = ASS(st.session_state.img, st.session_state.data[r], st.session_state.Orin[r])
                        if re == '0':
                            T[0].append("Governmental-حكومي")
                        elif re == '1':
                            T[0].append("Private-أهلي")
                        elif re == '2':
                            T[0].append("Tahfiz-تحفيظ")
                    elif r == 7:
                        re = ASS(st.session_state.img, st.session_state.data[r], st.session_state.Orin[r])
                        if re == '0':
                            T[0].append("Male-ذكر")
                        elif re == '1':
                            T[0].append("Female-أنثى")
                    elif r == 8:
                        re = ASS(st.session_state.img, st.session_state.data[r], st.session_state.Orin[r])
                        if re == '0':
                            T[0].append("Saudi-سعودي")
                        elif re == '1':
                            T[0].append("Non-Saudi-غيرسعودي")
                    elif r > 8:
                        re = ASS(st.session_state.img, st.session_state.data[r], st.session_state.Orin[r])
                        re = re.replace('3', 'A')
                        re = re.replace('2', 'B')
                        re = re.replace('1', 'C')
                        re = re.replace('0', 'D')
                        T[0].append("".join(re))
                    else:
                        T[0].append(ASS(st.session_state.img, st.session_state.data[r], st.session_state.Orin[r]))
                    # st.write(T)
                prog.empty()
        if start:
            # st.write(T)
            st.dataframe(pd.DataFrame(T, columns=st.session_state.Field))
    # N-ID
    if st.session_state.page == 1:
        st.header("Analysis تحليل (N-ID)")
        L1, L2 = st.columns(2)
        with L2:
            if st.button("Save-حفظ", type="primary", use_container_width=True):
                st.session_state.page = 2
                st._rerun()
            st.session_state.Field[st.session_state.page - 1] = st.text_input("Field-المجال", "National ID-رقم الهوية", 24)
            st.session_state.Orin[st.session_state.page - 1] = st.selectbox("Orientation-إتجاه الخلايا", ["Vertical", "Horizontal"],
                                                                            0)
            D1, D2 = st.columns(2)
            with D1:
                AC = st.slider("Amount of cells-عدد الخلايا", 1, 10, 10, )
                X = st.number_input("X-س", 0, len(st.session_state.img[1, :]), 152)
                H = st.number_input("H-الإرتفاع", 1, len(st.session_state.img[1, :]), 192)
                # HX = X + H
                # [ X , X + H , Y , Y + W , AC , AO]
            with D2:
                AO = st.slider("Amount of options-عدد الخيارات", 2, 10, 10)
                Y = st.number_input("Y-ص", 0, len(st.session_state.img[:, 1]), 368)
                W = st.number_input("W-العرض", 1, len(st.session_state.img[:, 1]), 190)
                # WY = Y + W
            st.session_state.data[st.session_state.page - 1] = [X, X + H, Y, Y + W, AC, AO]
        with L1:
            if st.button("Back", use_container_width=True):
                st.session_state.page = 0
                st._rerun()
            img = st.session_state.img.copy()
            rect = cv2.rectangle(img, [Y, X], [Y + W, X + H], 0, 10)
            st.image(rect, "AS-ورقة الحل")
            if st.checkbox("Scanning area-منطقة التحديد", True):
                st.image(st.session_state.img[X:X + H, Y:Y + W],
                         st.session_state.Field[st.session_state.page - 1] + ' Section')
            if st.checkbox("Sections-تقسيم الخلايا"):
                Col = st.columns(AC)
                if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                    # [X: H + X, Y: W + Y]
                    # [ X , X + H , Y , Y + W , AC , AO]
                    sh = int((Y + W - Y) / AC)
                    se = int(Y)
                    for t in range(AC):
                        with Col[t]:
                            st.image(
                                st.session_state.img[int(X):int(X + H),
                                se:se + sh], "S" + str(t))
                        se = se + sh
                elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                    sh = int((X + H - X) / AC)
                    se = int(X)
                    for t in range(AC):
                        # with Col[t]:
                        st.image(
                            st.session_state.img[se:se + sh,
                            int(Y):int(Y + W)], "S" + str(t))
                        se = se + sh
            if st.checkbox("Divide options-تقسيم الخلايا"):
                Col = st.columns(AC)
                if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                    sh = int((Y + W - Y) / AC)
                    se = int(Y)
                    for t in range(AC):
                        c_sh = int(
                            (X + H - X) / AO)
                        c_se = int(X)
                        for y in range(AO):
                            with Col[t]:
                                st.image((st.session_state.img[c_se:c_se + c_sh, se:se + sh]))
                            c_se = c_se + c_sh
                        se = se + sh

                elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                    sh = int((X + H - X) / AC)
                    se = int(X)
                    for t in range(AC):
                        c_sh = int(
                            (Y + W - Y) / AO)
                        c_se = int(Y)
                        for y in range(AO):
                            with Col[t]:
                                st.image((st.session_state.img[se:se + sh, c_se:c_se + c_sh]))
                            c_se = c_se + c_sh
                        se = se + sh
    # S-ID
    if st.session_state.page == 2:
        st.header("Analysis التحليل (S-ID)")
        L1, L2 = st.columns(2)
        with L2:
            if st.button("Save-حفظ", type="primary", use_container_width=True):
                st.session_state.page = 3  # U
                st._rerun()
            st.session_state.Field[st.session_state.page - 1] = st.text_input("Field-المجال", "School ID رقم المدرسة", 24)  # U
            st.session_state.Orin[st.session_state.page - 1] = st.selectbox("Orientation-إتجاه الخلايا", ["Vertical", "Horizontal"],
                                                                            0)  # U
            D1, D2 = st.columns(2)
            with D1:
                AC = st.slider("Amount of cells-عدد الخلايا", 1, 10, 5)  # U
                X = st.number_input("X-س", 0, len(st.session_state.img[1, :]), 152)  # U
                H = st.number_input("H-الارتفاع", 1, len(st.session_state.img[1, :]), 192)  # U
                # X+H = X + H
                # [ X , X + H , Y , Y + W , AC , AO]
            with D2:
                AO = st.slider("Amount of options-عدد الخيارات", 2, 10, 10)  # U
                Y = st.number_input("Y-ص", 0, len(st.session_state.img[:, 1]), 260)  # U
                W = st.number_input("W-العرض", 1, len(st.session_state.img[:, 1]), 99)  # U
                # Y+W = Y + W
            st.session_state.data[st.session_state.page - 1] = [X, X + H, Y, Y + W, AC, AO]
        with L1:
            if st.button("Back", use_container_width=True):  # U
                st.session_state.page = 1
                st._rerun()
            img = st.session_state.img.copy()
            rect = cv2.rectangle(img, [Y, X],
                                 [Y + W, X + H], 0, 10)
            st.image(rect, "AS-ورقة الحل")
            if st.checkbox("Scanning area-منطقة التحديد", True):
                st.image(st.session_state.img[X:X + H,
                         Y:Y + W], st.session_state.Field[st.session_state.page - 1])
            if st.checkbox("Sections-تقسيم الخلايا"):
                Col = st.columns(AC)
                if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                    # [X: H + X, Y: W + Y]
                    # [ X , X + H , Y , Y + W , AC , AO]
                    sh = int((Y + W - Y) / AC)
                    se = int(Y)
                    for t in range(AC):
                        with Col[t]:
                            st.image(
                                st.session_state.img[int(X):int(X + H),
                                se:se + sh], "S" + str(t))
                        se = se + sh
                elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                    sh = int((X + H - X) / AC)
                    se = int(X)
                    for t in range(AC):
                        # with Col[t]:
                        st.image(
                            st.session_state.img[se:se + sh,
                            int(Y):int(Y + W)], "S" + str(t))
                        se = se + sh
            if st.checkbox("Divide options-تقسيم الخلايا"):
                Col = st.columns(AC)
                if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                    sh = int((Y + W - Y) / AC)
                    se = int(Y)
                    for t in range(AC):
                        c_sh = int(
                            (X + H - X) / AO)
                        c_se = int(X)
                        for y in range(AO):
                            with Col[t]:
                                st.image((st.session_state.img[c_se:c_se + c_sh, se:se + sh]))
                            c_se = c_se + c_sh
                        se = se + sh

                elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                    sh = int((X + H - X) / AC)
                    se = int(X)
                    for t in range(AC):
                        c_sh = int(
                            (Y + W - Y) / AO)
                        c_se = int(Y)
                        for y in range(AO):
                            with Col[t]:
                                st.image((st.session_state.img[se:se + sh, c_se:c_se + c_sh]))
                            c_se = c_se + c_sh
                        se = se + sh
    # A-ID
    if st.session_state.page == 3:
        st.header("Analysis (A-ID)")
        L1, L2 = st.columns(2)
        with L2:
            if st.button("Save-حفظ", type="primary", use_container_width=True):
                st.session_state.page = 4  # U
                st._rerun()
            st.session_state.Field[st.session_state.page - 1] = st.text_input("Field-المجال", "Administration ID رقم الادارة", 24)  # U
            st.session_state.Orin[st.session_state.page - 1] = st.selectbox("Orientation-إتجاه الخلايا", ["Vertical", "Horizontal"],
                                                                            0)  # U
            D1, D2 = st.columns(2)
            with D1:
                AC = st.slider("Amount of cells-عدد الخلايا", 1, 10, 2)  # U
                X = st.number_input("X-س", 0, len(st.session_state.img[1, :]), 152)  # U
                H = st.number_input("H-الارتفاع", 1, len(st.session_state.img[1, :]), 192)  # U
                # X+H = X + H
                # [ X , X + H , Y , Y + W , AC , AO]
            with D2:
                AO = st.slider("Amount of options-عدد الخيارات", 2, 10, 10)  # U
                Y = st.number_input("Y-ص", 0, len(st.session_state.img[:, 1]), 209)  # U
                W = st.number_input("W-العرض", 1, len(st.session_state.img[:, 1]), 40)  # U
                # Y+W = Y + W
            st.session_state.data[st.session_state.page - 1] = [X, X + H, Y, Y + W, AC, AO]
        with L1:
            if st.button("Back", use_container_width=True):  # U
                st.session_state.page = 2
                st._rerun()
            img = st.session_state.img.copy()
            rect = cv2.rectangle(img, [Y, X],
                                 [Y + W, X + H], 0, 10)
            st.image(rect, "AS-ورقة الحل")
            if st.checkbox("Scanning area-منطقة التحديد", True):
                st.image(st.session_state.img[X:X + H,
                         Y:Y + W], st.session_state.Field[st.session_state.page - 1])
            if st.checkbox("Sections-تقسيم الخلايا"):
                Col = st.columns(AC)
                if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                    # [X: H + X, Y: W + Y]
                    # [ X , X + H , Y , Y + W , AC , AO]
                    sh = int((Y + W - Y) / AC)
                    se = int(Y)
                    for t in range(AC):
                        with Col[t]:
                            st.image(
                                st.session_state.img[int(X):int(X + H),
                                se:se + sh], "S" + str(t))
                        se = se + sh
                elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                    sh = int((X + H - X) / AC)
                    se = int(X)
                    for t in range(AC):
                        # with Col[t]:
                        st.image(
                            st.session_state.img[se:se + sh,
                            int(Y):int(Y + W)], "S" + str(t))
                        se = se + sh
            if st.checkbox("Divide options-تقسيم الخلايا"):
                Col = st.columns(AC)
                if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                    sh = int((Y + W - Y) / AC)
                    se = int(Y)
                    for t in range(AC):
                        c_sh = int(
                            (X + H - X) / AO)
                        c_se = int(X)
                        for y in range(AO):
                            with Col[t]:
                                st.image((st.session_state.img[c_se:c_se + c_sh, se:se + sh]))
                            c_se = c_se + c_sh
                        se = se + sh

                elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                    sh = int((X + H - X) / AC)
                    se = int(X)
                    for t in range(AC):
                        c_sh = int(
                            (Y + W - Y) / AO)
                        c_se = int(Y)
                        for y in range(AO):
                            with Col[t]:
                                st.image((st.session_state.img[se:se + sh, c_se:c_se + c_sh]))
                            c_se = c_se + c_sh
                        se = se + sh

    # Course
    if st.session_state.page == 4:
        st.header("Analysis (Co)")
        L1, L2 = st.columns(2)
        with L2:
            if st.button("Save-حفظ", type="primary", use_container_width=True):
                st.session_state.page = 5  # U
                st._rerun()
            st.session_state.Field[st.session_state.page - 1] = st.text_input("Field-المجال", "Course", 24)  # U
            st.session_state.Orin[st.session_state.page - 1] = st.selectbox("Orientation-إتجاه الخلايا", ["Vertical", "Horizontal"],
                                                                            0)  # U
            D1, D2 = st.columns(2)
            with D1:
                AC = st.slider("Amount of cells-عدد الخلايا", 1, 10, 1)  # U
                X = st.number_input("X-س", 0, len(st.session_state.img[1, :]), 380)  # U
                H = st.number_input("H-الارتفاع", 1, len(st.session_state.img[1, :]), 52)  # U
                # X+H = X + H
                # [ X , X + H , Y , Y + W , AC , AO]
            with D2:
                AO = st.slider("Amount of options-عدد الخيارات", 2, 10, 3)  # U
                Y = st.number_input("Y-ص", 0, len(st.session_state.img[:, 1]), 540)  # U
                W = st.number_input("W-العرض", 1, len(st.session_state.img[:, 1]), 17)  # U
                # Y+W = Y + W
            st.session_state.data[st.session_state.page - 1] = [X, X + H, Y, Y + W, AC, AO]
        with L1:
            if st.button("Back", use_container_width=True):
                st.session_state.page = 3  # U
                st._rerun()
            img = st.session_state.img.copy()
            rect = cv2.rectangle(img, [Y, X],
                                 [Y + W, X + H], 0, 5)
            st.image(rect, "AS-ورقة الحل")
            if st.checkbox("Scanning area-منطقة التحديد", True):
                st.image(st.session_state.img[X:X + H,
                         Y:Y + W], st.session_state.Field[st.session_state.page - 1])
            if st.checkbox("Sections-تقسيم الخلايا"):
                Col = st.columns(AC)
                if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                    # [ X : H + X , Y : W + Y ]
                    # [ X , X + H , Y , Y + W , AC , AO]
                    sh = int((Y + W - Y) / AC)
                    se = int(Y)
                    for t in range(AC):
                        with Col[t]:
                            st.image(
                                st.session_state.img[int(X):int(X + H),
                                se:se + sh], "S" + str(t))
                        se = se + sh
                elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                    sh = int((X + H - X) / AC)
                    se = int(X)
                    for t in range(AC):
                        # with Col[t]:
                        st.image(
                            st.session_state.img[se:se + sh,
                            int(Y):int(Y + W)], "S" + str(t))
                        se = se + sh
            if st.checkbox("Divide options-تقسيم الخلايا"):
                Col = st.columns(AC)
                if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                    sh = int((Y + W - Y) / AC)
                    se = int(Y)
                    for t in range(AC):
                        c_sh = int(
                            (X + H - X) / AO)
                        c_se = int(X)
                        for y in range(AO):
                            with Col[t]:
                                st.image((st.session_state.img[c_se:c_se + c_sh, se:se + sh]))
                            c_se = c_se + c_sh
                        se = se + sh

                elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                    sh = int((X + H - X) / AC)
                    se = int(X)
                    for t in range(AC):
                        c_sh = int(
                            (Y + W - Y) / AO)
                        c_se = int(Y)
                        for y in range(AO):
                            with Col[t]:
                                st.image((st.session_state.img[se:se + sh, c_se:c_se + c_sh]))
                            c_se = c_se + c_sh
                        se = se + sh
    # Grade
    if st.session_state.page == 5:
        st.header("Analysis (Gr)")  # U
        L1, L2 = st.columns(2)
        with L2:
            if st.button("Save-حفظ", type="primary", use_container_width=True):
                st.session_state.page = 6  # U
                st._rerun()
            st.session_state.Field[st.session_state.page - 1] = st.text_input("Field-المجال", "Student Grade", 24)  # U
            st.session_state.Orin[st.session_state.page - 1] = st.selectbox("Orientation-إتجاه الخلايا", ["Vertical", "Horizontal"],
                                                                            0)  # U
            D1, D2 = st.columns(2)
            with D1:
                AC = st.slider("Amount of cells-عدد الخلايا", 1, 10, 1)  # U
                X = st.number_input("X-س", 0, len(st.session_state.img[1, :]), 380)  # U
                H = st.number_input("H-الارتفاع", 1, len(st.session_state.img[1, :]), 52)  # U
                # X+H = X + H
                # [ X , X + H , Y , Y + W , AC , AO]
            with D2:
                AO = st.slider("Amount of options-عدد الخيارات", 2, 10, 2)  # U
                Y = st.number_input("Y-ص", 0, len(st.session_state.img[:, 1]), 477)  # U
                W = st.number_input("W-العرض", 1, len(st.session_state.img[:, 1]), 17)  # U
                # Y+W = Y + W
            st.session_state.data[st.session_state.page - 1] = [X, X + H, Y, Y + W, AC, AO]
        with L1:
            if st.button("Back", use_container_width=True):  # U
                st.session_state.page = 4
                st._rerun()
            img = st.session_state.img.copy()
            rect = cv2.rectangle(img, [Y, X],
                                 [Y + W, X + H], 0, 10)
            st.image(rect, "AS-ورقة الحل")
            if st.checkbox("Scanning area-منطقة التحديد", True):
                st.image(st.session_state.img[X:X + H,
                         Y:Y + W], st.session_state.Field[st.session_state.page - 1])
            if st.checkbox("Sections-تقسيم الخلايا"):
                Col = st.columns(AC)
                if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                    # [X: H + X, Y: W + Y]
                    # [ X , X + H , Y , Y + W , AC , AO]
                    sh = int((Y + W - Y) / AC)
                    se = int(Y)
                    for t in range(AC):
                        with Col[t]:
                            st.image(
                                st.session_state.img[int(X):int(X + H),
                                se:se + sh], "S" + str(t))
                        se = se + sh
                elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                    sh = int((X + H - X) / AC)
                    se = int(X)
                    for t in range(AC):
                        # with Col[t]:
                        st.image(
                            st.session_state.img[se:se + sh,
                            int(Y):int(Y + W)], "S" + str(t))
                        se = se + sh
            if st.checkbox("Divide options-تقسيم الخلايا"):
                Col = st.columns(AC)
                if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                    sh = int((Y + W - Y) / AC)
                    se = int(Y)
                    for t in range(AC):
                        c_sh = int(
                            (X + H - X) / AO)
                        c_se = int(X)
                        for y in range(AO):
                            with Col[t]:
                                st.image((st.session_state.img[c_se:c_se + c_sh, se:se + sh]))
                            c_se = c_se + c_sh
                        se = se + sh

                elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                    sh = int((X + H - X) / AC)
                    se = int(X)
                    for t in range(AC):
                        c_sh = int(
                            (Y + W - Y) / AO)
                        c_se = int(Y)
                        for y in range(AO):
                            with Col[t]:
                                st.image((st.session_state.img[se:se + sh, c_se:c_se + c_sh]))
                            c_se = c_se + c_sh
                        se = se + sh
    # Form
    if st.session_state.page == 6:
        st.header("Analysis (Fo)")
        L1, L2 = st.columns(2)
        with L2:
            if st.button("Save-حفظ", type="primary", use_container_width=True):
                st.session_state.page = 7  # U
                st._rerun()
            st.session_state.Field[st.session_state.page - 1] = st.text_input("Field-المجال", "Form", 24)  # U
            st.session_state.Orin[st.session_state.page - 1] = st.selectbox("Orientation-إتجاه الخلايا", ["Vertical", "Horizontal"],
                                                                            0)  # U
            D1, D2 = st.columns(2)
            with D1:
                AC = st.slider("Amount of cells-عدد الخلايا", 1, 10, 1)  # U
                X = st.number_input("X-س", 0, len(st.session_state.img[1, :]), 380)  # U
                H = st.number_input("H-الارتفاع", 1, len(st.session_state.img[1, :]), 52)  # U
                # X+H = X + H
                # [ X , X + H , Y , Y + W , AC , AO]
            with D2:
                AO = st.slider("Amount of options-عدد الخيارات", 2, 10, 3)  # U
                Y = st.number_input("Y-ص", 0, len(st.session_state.img[:, 1]), 380)  # U
                W = st.number_input("W-العرض", 1, len(st.session_state.img[:, 1]), 17)  # U
                # Y+W = Y + W
            st.session_state.data[st.session_state.page - 1] = [X, X + H, Y, Y + W, AC, AO]
        with L1:
            if st.button("Back", use_container_width=True):  # U
                st.session_state.page = 5
                st._rerun()
            img = st.session_state.img.copy()
            rect = cv2.rectangle(img, [Y, X],
                                 [Y + W, X + H], 0, 10)
            st.image(rect, "AS-ورقة الحل")
            if st.checkbox("Scanning area-منطقة التحديد", True):
                st.image(st.session_state.img[X:X + H,
                         Y:Y + W], st.session_state.Field[st.session_state.page - 1])
            if st.checkbox("Sections-تقسيم الخلايا"):
                Col = st.columns(AC)
                if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                    # [X: H + X, Y: W + Y]
                    # [ X , X + H , Y , Y + W , AC , AO]
                    sh = int((Y + W - Y) / AC)
                    se = int(Y)
                    for t in range(AC):
                        with Col[t]:
                            st.image(
                                st.session_state.img[int(X):int(X + H),
                                se:se + sh], "S" + str(t))
                        se = se + sh
                elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                    sh = int((X + H - X) / AC)
                    se = int(X)
                    for t in range(AC):
                        # with Col[t]:
                        st.image(
                            st.session_state.img[se:se + sh,
                            int(Y):int(Y + W)], "S" + str(t))
                        se = se + sh
            if st.checkbox("Divide options-تقسيم الخلايا"):
                Col = st.columns(AC)
                if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                    sh = int((Y + W - Y) / AC)
                    se = int(Y)
                    for t in range(AC):
                        c_sh = int(
                            (X + H - X) / AO)
                        c_se = int(X)
                        for y in range(AO):
                            with Col[t]:
                                st.image((st.session_state.img[c_se:c_se + c_sh, se:se + sh]))
                            c_se = c_se + c_sh
                        se = se + sh

                elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                    sh = int((X + H - X) / AC)
                    se = int(X)
                    for t in range(AC):
                        c_sh = int((Y + W - Y) / AO)
                        c_se = int(Y)
                        for y in range(AO):
                            with Col[t]:
                                st.image((st.session_state.img[se:se + sh, c_se:c_se + c_sh]))
                            c_se = c_se + c_sh
                        se = se + sh
    # Type
    if st.session_state.page == 7:
        st.header("Analysis (Ty)")
        L1, L2 = st.columns(2)
        with L2:
            if st.button("Save-حفظ", type="primary", use_container_width=True):
                st.session_state.page = 8  # U
                st._rerun()
            st.session_state.Field[st.session_state.page - 1] = st.text_input("Field-المجال", "School type", 24)  # U
            st.session_state.Orin[st.session_state.page - 1] = st.selectbox("Orientation-إتجاه الخلايا", ["Vertical", "Horizontal"],
                                                                            0)  # U
            D1, D2 = st.columns(2)
            with D1:
                AC = st.slider("Amount of cells-عدد الخلايا", 1, 10, 1)  # U
                X = st.number_input("X-س", 0, len(st.session_state.img[1, :]), 373)  # U
                H = st.number_input("H-الارتفاع", 1, len(st.session_state.img[1, :]), 52)  # U
                # X+H = X + H
                # [ X , X + H , Y , Y + W , AC , AO]
            with D2:
                AO = st.slider("Amount of options-عدد الخيارات", 2, 10, 3)  # U
                Y = st.number_input("Y-ص", 0, len(st.session_state.img[:, 1]), 347)  # U
                W = st.number_input("W-العرض", 1, len(st.session_state.img[:, 1]), 17)  # U
                # Y+W = Y + W
            st.session_state.data[st.session_state.page - 1] = [X, X + H, Y, Y + W, AC, AO]
        with L1:
            if st.button("Back", use_container_width=True):  # U
                st.session_state.page = 6
                st._rerun()
            img = st.session_state.img.copy()
            rect = cv2.rectangle(img, [Y, X],
                                 [Y + W, X + H], 0, 10)
            st.image(rect, "AS-ورقة الحل")
            if st.checkbox("Scanning area-منطقة التحديد", True):
                st.image(st.session_state.img[X:X + H,
                         Y:Y + W], st.session_state.Field[st.session_state.page - 1])
            if st.checkbox("Sections-تقسيم الخلايا"):
                Col = st.columns(AC)
                if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                    # [X: H + X, Y: W + Y]
                    # [ X , X + H , Y , Y + W , AC , AO]
                    sh = int((Y + W - Y) / AC)
                    se = int(Y)
                    for t in range(AC):
                        with Col[t]:
                            st.image(
                                st.session_state.img[int(X):int(X + H),
                                se:se + sh], "S" + str(t))
                        se = se + sh
                elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                    sh = int((X + H - X) / AC)
                    se = int(X)
                    for t in range(AC):
                        # with Col[t]:
                        st.image(
                            st.session_state.img[se:se + sh,
                            int(Y):int(Y + W)], "S" + str(t))
                        se = se + sh
            if st.checkbox("Divide options-تقسيم الخلايا"):
                Col = st.columns(AC)
                if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                    sh = int((Y + W - Y) / AC)
                    se = int(Y)
                    for t in range(AC):
                        c_sh = int(
                            (X + H - X) / AO)
                        c_se = int(X)
                        for y in range(AO):
                            with Col[t]:
                                st.image((st.session_state.img[c_se:c_se + c_sh, se:se + sh]))
                            c_se = c_se + c_sh
                        se = se + sh

                elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                    sh = int((X + H - X) / AC)
                    se = int(X)
                    for t in range(AC):
                        c_sh = int(
                            (Y + W - Y) / AO)
                        c_se = int(Y)
                        for y in range(AO):
                            with Col[t]:
                                st.image((st.session_state.img[se:se + sh, c_se:c_se + c_sh]))
                            c_se = c_se + c_sh
                        se = se + sh
    # Se
    if st.session_state.page == 8:
        st.header("Analysis (Se)")
        L1, L2 = st.columns(2)
        with L2:
            if st.button("Save-حفظ", type="primary", use_container_width=True):
                st.session_state.page = 9  # U
                st._rerun()
            st.session_state.Field[st.session_state.page - 1] = st.text_input("Field-المجال", "Sex", 24)  # U
            st.session_state.Orin[st.session_state.page - 1] = st.selectbox("Orientation-إتجاه الخلايا", ["Vertical", "Horizontal"],
                                                                            0)  # U
            D1, D2 = st.columns(2)
            with D1:
                AC = st.slider("Amount of cells-عدد الخلايا", 1, 10, 1)  # U
                X = st.number_input("X-س", 0, len(st.session_state.img[1, :]), 380)  # U
                H = st.number_input("H-الارتفاع", 1, len(st.session_state.img[1, :]), 52)  # U
                # X+H = X + H
                # [ X , X + H , Y , Y + W , AC , AO]
            with D2:
                AO = st.slider("Amount of options-عدد الخيارات", 2, 10, 2)  # U
                Y = st.number_input("Y-ص", 0, len(st.session_state.img[:, 1]), 292)  # U
                W = st.number_input("W-العرض", 1, len(st.session_state.img[:, 1]), 17)  # U
                # Y+W = Y + W
            st.session_state.data[st.session_state.page - 1] = [X, X + H, Y, Y + W, AC, AO]

        with L1:
            if st.button("Back", use_container_width=True):  # U
                st.session_state.page = 7
                st._rerun()
            img = st.session_state.img.copy()
            rect = cv2.rectangle(img, [Y, X],
                                 [Y + W, X + H], 0, 10)
            st.image(rect, "AS-ورقة الحل")
            if st.checkbox("Scanning area-منطقة التحديد", True):
                st.image(st.session_state.img[X:X + H,
                         Y:Y + W], st.session_state.Field[st.session_state.page - 1])
            if st.checkbox("Sections-تقسيم الخلايا"):
                Col = st.columns(AC)
                if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                    # [X: H + X, Y: W + Y]
                    # [ X , X + H , Y , Y + W , AC , AO]
                    sh = int((Y + W - Y) / AC)
                    se = int(Y)
                    for t in range(AC):
                        with Col[t]:
                            st.image(
                                st.session_state.img[int(X):int(X + H),
                                se:se + sh], "S" + str(t))
                        se = se + sh
                elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                    sh = int((X + H - X) / AC)
                    se = int(X)
                    for t in range(AC):
                        # with Col[t]:
                        st.image(
                            st.session_state.img[se:se + sh,
                            int(Y):int(Y + W)], "S" + str(t))
                        se = se + sh
            if st.checkbox("Divide options-تقسيم الخلايا"):
                Col = st.columns(AC)
                if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                    sh = int((Y + W - Y) / AC)
                    se = int(Y)
                    for t in range(AC):
                        c_sh = int(
                            (X + H - X) / AO)
                        c_se = int(X)
                        for y in range(AO):
                            with Col[t]:
                                st.image((st.session_state.img[c_se:c_se + c_sh, se:se + sh]))
                            c_se = c_se + c_sh
                        se = se + sh

                elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                    sh = int((X + H - X) / AC)
                    se = int(X)
                    for t in range(AC):
                        c_sh = int(
                            (Y + W - Y) / AO)
                        c_se = int(Y)
                        for y in range(AO):
                            with Col[t]:
                                st.image((st.session_state.img[se:se + sh, c_se:c_se + c_sh]))
                            c_se = c_se + c_sh
                        se = se + sh
    # Na
    if st.session_state.page == 9:
        st.header("Analysis (Na)")
        L1, L2 = st.columns(2)
        with L2:
            if st.button("Save-حفظ", type="primary", use_container_width=True):
                st.session_state.page = 10  # U
                st._rerun()
            st.session_state.Field[st.session_state.page - 1] = st.text_input("Field-المجال", "Nationality", 24)  # U
            st.session_state.Orin[st.session_state.page - 1] = st.selectbox("Orientation-إتجاه الخلايا", ["Vertical", "Horizontal"],
                                                                            0)  # U
            D1, D2 = st.columns(2)
            with D1:
                AC = st.slider("Amount of cells-عدد الخلايا", 1, 10, 1)  # U
                X = st.number_input("X-س", 0, len(st.session_state.img[1, :]), 373)  # U
                H = st.number_input("H-الارتفاع", 1, len(st.session_state.img[1, :]), 52)  # U
                # X+H = X + H
                # [ X , X + H , Y , Y + W , AC , AO]
            with D2:
                AO = st.slider("Amount of options-عدد الخيارات", 2, 10, 2)  # U
                Y = st.number_input("Y-ص", 0, len(st.session_state.img[:, 1]), 252)  # U
                W = st.number_input("W-العرض", 1, len(st.session_state.img[:, 1]), 17)  # U
                # Y+W = Y + W
                st.session_state.data[st.session_state.page - 1] = [X, X + H, Y, Y + W, AC, AO]

        with L1:
            if st.button("Back", use_container_width=True):  # U
                st.session_state.page = 8
                st._rerun()
            img = st.session_state.img.copy()
            rect = cv2.rectangle(img, [Y, X],
                                 [Y + W, X + H], 0, 10)
            st.image(rect, "AS-ورقة الحل")
            if st.checkbox("Scanning area-منطقة التحديد", True):
                st.image(st.session_state.img[X:X + H,
                         Y:Y + W], st.session_state.Field[st.session_state.page - 1])
            if st.checkbox("Sections-تقسيم الخلايا"):
                Col = st.columns(AC)
                if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                    # [X: H + X, Y: W + Y]
                    # [ X , X + H , Y , Y + W , AC , AO]
                    sh = int((Y + W - Y) / AC)
                    se = int(Y)
                    for t in range(AC):
                        with Col[t]:
                            st.image(
                                st.session_state.img[int(X):int(X + H),
                                se:se + sh], "S" + str(t))
                        se = se + sh
                elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                    sh = int((X + H - X) / AC)
                    se = int(X)
                    for t in range(AC):
                        # with Col[t]:
                        st.image(
                            st.session_state.img[se:se + sh,
                            int(Y):int(Y + W)], "S" + str(t))
                        se = se + sh
            if st.checkbox("Divide options-تقسيم الخلايا"):
                Col = st.columns(AC)
                if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                    sh = int((Y + W - Y) / AC)
                    se = int(Y)
                    for t in range(AC):
                        c_sh = int(
                            (X + H - X) / AO)
                        c_se = int(X)
                        for y in range(AO):
                            with Col[t]:
                                st.image((st.session_state.img[c_se:c_se + c_sh, se:se + sh]))
                            c_se = c_se + c_sh
                        se = se + sh
                elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                    sh = int((X + H - X) / AC)
                    se = int(X)
                    for t in range(AC):
                        c_sh = int(
                            (Y + W - Y) / AO)
                        c_se = int(Y)
                        for y in range(AO):
                            with Col[t]:
                                st.image((st.session_state.img[se:se + sh, c_se:c_se + c_sh]))
                            c_se = c_se + c_sh
                        se = se + sh

    # Answers
    if st.session_state.page == 10:
        st.header("Analysis (A1)")
        L1, L2 = st.columns(2)
        with L2:
            if st.button("Save-حفظ", type="primary", use_container_width=True):
                st.session_state.page = 11  # U
                st._rerun()
            st.session_state.Field[st.session_state.page - 1] = st.text_input("Field-المجال", "Answers 1", 24)  # U
            st.session_state.Orin[st.session_state.page - 1] = st.selectbox("Orientation-إتجاه الخلايا", ["Vertical", "Horizontal"],
                                                                            1)  # U
            D1, D2 = st.columns(2)
            with D1:
                AC = st.slider("Amount of cells-عدد الخلايا", 1, 20, 15)  # U
                X = st.number_input("X-س", 0, len(st.session_state.img[1, :]), 525)  # U
                H = st.number_input("H-الارتفاع", 1, len(st.session_state.img[1, :]), 290)  # U
                # X+H = X + H
                # [ X , X + H , Y , Y + W , AC , AO]
            with D2:
                AO = st.slider("Amount of options-عدد الخيارات", 2, 10, 4)  # U
                Y = st.number_input("Y-ص", 0, len(st.session_state.img[:, 1]), 444)  # U
                W = st.number_input("W-العرض", 1, len(st.session_state.img[:, 1]), 90)  # U
                # Y+W = Y + W
                st.session_state.data[st.session_state.page - 1] = [X, X + H, Y, Y + W, AC, AO]

        with L1:
            if st.button("Back", use_container_width=True):  # U
                st.session_state.page = 9
                st._rerun()
            img = st.session_state.img.copy()
            rect = cv2.rectangle(img, [Y, X],
                                 [Y + W, X + H], 0, 10)
            st.image(rect, "AS-ورقة الحل")
        if st.checkbox("Scanning area-منطقة التحديد", True):
            st.image(st.session_state.img[X:X + H,
                     Y:Y + W], st.session_state.Field[st.session_state.page - 1])
        if st.checkbox("Sections-تقسيم الخلايا"):
            Col = st.columns(AC)
            if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                # [X: H + X, Y: W + Y]
                # [ X , X + H , Y , Y + W , AC , AO]
                sh = int((Y + W - Y) / AC)
                se = int(Y)
                for t in range(AC):
                    with Col[t]:
                        st.image(
                            st.session_state.img[int(X):int(X + H),
                            se:se + sh], "S" + str(t))
                    se = se + sh
            elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                sh = int((X + H - X) / AC)
                se = int(X)
                for t in range(AC):
                    # with Col[t]:
                    st.image(
                        st.session_state.img[se:se + sh,
                        int(Y):int(Y + W)], "S" + str(t))
                    se = se + sh
        if st.checkbox("Divide options-تقسيم الخلايا"):
            Col = st.columns(AC)
            if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                sh = int((Y + W - Y) / AC)
                se = int(Y)
                for t in range(AC):
                    c_sh = int(
                        (X + H - X) / AO)
                    c_se = int(X)
                    for y in range(AO):
                        with Col[t]:
                            st.image((st.session_state.img[c_se:c_se + c_sh, se:se + sh]))
                        c_se = c_se + c_sh
                    se = se + sh
            elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                sh = int((X + H - X) / AC)
                se = int(X)
                for t in range(AC):
                    c_sh = int(
                        (Y + W - Y) / AO)
                    c_se = int(Y)
                    for y in range(AO):
                        with Col[t]:
                            st.image((st.session_state.img[se:se + sh, c_se:c_se + c_sh]))
                        c_se = c_se + c_sh
                    se = se + sh
    if st.session_state.page == 11:
        st.header("Analysis (A2)")
        L1, L2 = st.columns(2)
        with L2:
            if st.button("Save-حفظ", type="primary", use_container_width=True):
                st.session_state.page = 12  # U
                st._rerun()
            st.session_state.Field[st.session_state.page - 1] = st.text_input("Field-المجال", "Answers 2", 24)  # U
            st.session_state.Orin[st.session_state.page - 1] = st.selectbox("Orientation-إتجاه الخلايا", ["Vertical", "Horizontal"],
                                                                            1)  # U
            D1, D2 = st.columns(2)
            with D1:
                AC = st.slider("Amount of cells-عدد الخلايا", 1, 20, 15)  # U
                X = st.number_input("X-س", 0, len(st.session_state.img[1, :]), 525)  # U
                H = st.number_input("H-الارتفاع", 1, len(st.session_state.img[1, :]), 290)  # U
                # X+H = X + H
                # [ X , X + H , Y , Y + W , AC , AO]
            with D2:
                AO = st.slider("Amount of options-عدد الخيارات", 2, 10, 4)  # U
                Y = st.number_input("Y-ص", 0, len(st.session_state.img[:, 1]), 315)  # U
                W = st.number_input("W-العرض", 1, len(st.session_state.img[:, 1]), 90)  # U
                # Y+W = Y + W
                st.session_state.data[st.session_state.page - 1] = [X, X + H, Y, Y + W, AC, AO]

        with L1:
            if st.button("Back", use_container_width=True):  # U
                st.session_state.page = 10
                st._rerun()
            img = st.session_state.img.copy()
            rect = cv2.rectangle(img, [Y, X],
                                 [Y + W, X + H], 0, 10)
            st.image(rect, "AS-ورقة الحل")
        if st.checkbox("Scanning area-منطقة التحديد", True):
            st.image(st.session_state.img[X:X + H,
                     Y:Y + W], st.session_state.Field[st.session_state.page - 1])
        if st.checkbox("Sections-تقسيم الخلايا"):
            Col = st.columns(AC)
            if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                # [X: H + X, Y: W + Y]
                # [ X , X + H , Y , Y + W , AC , AO]
                sh = int((Y + W - Y) / AC)
                se = int(Y)
                for t in range(AC):
                    with Col[t]:
                        st.image(
                            st.session_state.img[int(X):int(X + H),
                            se:se + sh], "S" + str(t))
                    se = se + sh
            elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                sh = int((X + H - X) / AC)
                se = int(X)
                for t in range(AC):
                    # with Col[t]:
                    st.image(
                        st.session_state.img[se:se + sh,
                        int(Y):int(Y + W)], "S" + str(t))
                    se = se + sh
        if st.checkbox("Divide options-تقسيم الخلايا"):
            Col = st.columns(AC)
            if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                sh = int((Y + W - Y) / AC)
                se = int(Y)
                for t in range(AC):
                    c_sh = int(
                        (X + H - X) / AO)
                    c_se = int(X)
                    for y in range(AO):
                        with Col[t]:
                            st.image((st.session_state.img[c_se:c_se + c_sh, se:se + sh]))
                        c_se = c_se + c_sh
                    se = se + sh
            elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                sh = int((X + H - X) / AC)
                se = int(X)
                for t in range(AC):
                    c_sh = int(
                        (Y + W - Y) / AO)
                    c_se = int(Y)
                    for y in range(AO):
                        with Col[t]:
                            st.image((st.session_state.img[se:se + sh, c_se:c_se + c_sh]))
                        c_se = c_se + c_sh
                    se = se + sh
    if st.session_state.page == 12:
        st.header("Analysis (A3)")
        L1, L2 = st.columns(2)
        with L2:
            if st.button("Save-حفظ", type="primary", use_container_width=True):
                st.session_state.page = 13  # U
                st._rerun()
            st.session_state.Field[st.session_state.page - 1] = st.text_input("Field-المجال", "Answers 3", 24)  # U
            st.session_state.Orin[st.session_state.page - 1] = st.selectbox("Orientation-إتجاه الخلايا", ["Vertical", "Horizontal"],
                                                                            1)  # U
            D1, D2 = st.columns(2)
            with D1:
                AC = st.slider("Amount of cells-عدد الخلايا", 1, 20, 15)  # U
                X = st.number_input("X-س", 0, len(st.session_state.img[1, :]), 525)  # U
                H = st.number_input("H-الارتفاع", 1, len(st.session_state.img[1, :]), 290)  # U
                # X+H = X + H
                # [ X , X + H , Y , Y + W , AC , AO]
            with D2:
                AO = st.slider("Amount of options-عدد الخيارات", 2, 10, 4)  # U
                Y = st.number_input("Y-ص", 0, len(st.session_state.img[:, 1]), 187)  # U
                W = st.number_input("W-العرض", 1, len(st.session_state.img[:, 1]), 90)  # U
                # Y+W = Y + W
                st.session_state.data[st.session_state.page - 1] = [X, X + H, Y, Y + W, AC, AO]

        with L1:
            if st.button("Back", use_container_width=True):  # U
                st.session_state.page = 11
                st._rerun()
            img = st.session_state.img.copy()
            rect = cv2.rectangle(img, [Y, X],
                                 [Y + W, X + H], 0, 10)
            st.image(rect, "AS-ورقة الحل")
        if st.checkbox("Scanning area-منطقة التحديد", True):
            st.image(st.session_state.img[X:X + H,
                     Y:Y + W], st.session_state.Field[st.session_state.page - 1])
        if st.checkbox("Sections-تقسيم الخلايا"):
            Col = st.columns(AC)
            if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                # [X: H + X, Y: W + Y]
                # [ X , X + H , Y , Y + W , AC , AO]
                sh = int((Y + W - Y) / AC)
                se = int(Y)
                for t in range(AC):
                    with Col[t]:
                        st.image(
                            st.session_state.img[int(X):int(X + H),
                            se:se + sh], "S" + str(t))
                    se = se + sh
            elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                sh = int((X + H - X) / AC)
                se = int(X)
                for t in range(AC):
                    # with Col[t]:
                    st.image(
                        st.session_state.img[se:se + sh,
                        int(Y):int(Y + W)], "S" + str(t))
                    se = se + sh
        if st.checkbox("Divide options-تقسيم الخلايا"):
            Col = st.columns(AC)
            if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                sh = int((Y + W - Y) / AC)
                se = int(Y)
                for t in range(AC):
                    c_sh = int(
                        (X + H - X) / AO)
                    c_se = int(X)
                    for y in range(AO):
                        with Col[t]:
                            st.image((st.session_state.img[c_se:c_se + c_sh, se:se + sh]))
                        c_se = c_se + c_sh
                    se = se + sh
            elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                sh = int((X + H - X) / AC)
                se = int(X)
                for t in range(AC):
                    c_sh = int(
                        (Y + W - Y) / AO)
                    c_se = int(Y)
                    for y in range(AO):
                        with Col[t]:
                            st.image((st.session_state.img[se:se + sh, c_se:c_se + c_sh]))
                        c_se = c_se + c_sh
                    se = se + sh
    if st.session_state.page == 13:
        st.header("Analysis (A4)")
        L1, L2 = st.columns(2)
        with L2:
            if st.button("Submit", type="primary", use_container_width=True):
                if st.session_state.input_im == "Example نموذج":
                    st.session_state.sup = 0
                elif st.session_state.input_im == "Solved Ex نموذج محلول":
                    st.session_state.sup = 1
                elif st.session_state.input_im == "Upload ارفع الملف":
                    st.session_state.sup = 2
                st.session_state.page = 0  # U
                st._rerun()
            st.session_state.Field[st.session_state.page - 1] = st.text_input("Field-المجال", "Answers 4", 24)  # U
            st.session_state.Orin[st.session_state.page - 1] = st.selectbox("Orientation-إتجاه الخلايا", ["Vertical", "Horizontal"],
                                                                            1)  # U
            D1, D2 = st.columns(2)
            with D1:
                AC = st.slider("Amount of cells-عدد الخلايا", 1, 20, 15)  # U
                X = st.number_input("X-س", 0, len(st.session_state.img[1, :]), 525)  # U
                H = st.number_input("H-الارتفاع", 1, len(st.session_state.img[1, :]), 290)  # U
                # X+H = X + H
                # [ X , X + H , Y , Y + W , AC , AO]
            with D2:
                AO = st.slider("Amount of options-عدد الخيارات", 2, 10, 4)  # U
                Y = st.number_input("Y-ص", 0, len(st.session_state.img[:, 1]), 56)  # U
                W = st.number_input("W-العرض", 1, len(st.session_state.img[:, 1]), 90)  # U
                # Y+W = Y + W
                st.session_state.data[st.session_state.page - 1] = [X, X + H, Y, Y + W, AC, AO]

        with L1:
            if st.button("Back", use_container_width=True):  # U
                st.session_state.page = 12
                st._rerun()
            img = st.session_state.img.copy()
            rect = cv2.rectangle(img, [Y, X],
                                 [Y + W, X + H], 0, 10)
            st.image(rect, "AS-ورقة الحل")
        if st.checkbox("Scanning area-منطقة التحديد", True):
            st.image(st.session_state.img[X:X + H,
                     Y:Y + W], st.session_state.Field[st.session_state.page - 1])
        if st.checkbox("Sections-تقسيم الخلايا"):
            Col = st.columns(AC)
            if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                # [X: H + X, Y: W + Y]
                # [ X , X + H , Y , Y + W , AC , AO]
                sh = int((Y + W - Y) / AC)
                se = int(Y)
                for t in range(AC):
                    with Col[t]:
                        st.image(
                            st.session_state.img[int(X):int(X + H),
                            se:se + sh], "S" + str(t))
                    se = se + sh
            elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                sh = int((X + H - X) / AC)
                se = int(X)
                for t in range(AC):
                    # with Col[t]:
                    st.image(
                        st.session_state.img[se:se + sh,
                        int(Y):int(Y + W)], "S" + str(t))
                    se = se + sh
        if st.checkbox("Divide options-تقسيم الخلايا"):
            Col = st.columns(AC)
            if st.session_state.Orin[st.session_state.page - 1] == "Vertical":
                sh = int((Y + W - Y) / AC)
                se = int(Y)
                for t in range(AC):
                    c_sh = int(
                        (X + H - X) / AO)
                    c_se = int(X)
                    for y in range(AO):
                        with Col[t]:
                            st.image((st.session_state.img[c_se:c_se + c_sh, se:se + sh]))
                        c_se = c_se + c_sh
                    se = se + sh
            elif st.session_state.Orin[st.session_state.page - 1] == "Horizontal":
                sh = int((X + H - X) / AC)
                se = int(X)
                for t in range(AC):
                    c_sh = int(
                        (Y + W - Y) / AO)
                    c_se = int(Y)
                    for y in range(AO):
                        with Col[t]:
                            st.image((st.session_state.img[se:se + sh, c_se:c_se + c_sh]))
                        c_se = c_se + c_sh
                    se = se + sh
