import streamlit as st
import gettext


# Function to set up the localizator
def set_localization(language):
    try:
        localizator = gettext.translation(
            f"base_{language}", localedir="locales", languages=[language]
        )
        localizator.install()
        _ = localizator.gettext
    except Exception:
        # st.error(f"Translation error: {e}")
        _ = gettext.gettext
    return _


def available_languages():
    languages_dict = {
        "english": "🇺🇸 English",
        "zh-TW": "🇹🇼 繁體中文",
        "zh-CN": "🇨🇳 簡体中文",
        # "ja": "🇯🇵 日本語",
    }

    languages = [language for language in languages_dict]
    st.session_state.language = st.sidebar.selectbox(
        " ",
        languages,
        format_func=lambda x: languages_dict.get(x),
    )

    _ = set_localization(st.session_state.language)


try:
    _ = set_localization(st.session_state.language)
except Exception:
    _ = set_localization("english")


def back_to_home(selected_language):
    _ = set_localization(selected_language)
    st.html(
        """<style>
            div[data-testid="stPageLink"] p::before { 
                font-family: "Font Awesome 5 Free" !important;
                content: "\\f015";
                display: inline-block;
                vertical-align: middle;
                font-weight: 700;
                font-size: 18px;
                font-family: 'Baloo 2';
                color: white;
                padding-right: 8px;
            }
            div[data-testid="stPageLink"] p { 
                position: absolute;
                right: 50%;
                transform: translateX(50%);
                padding: 3px 10px;
                font-weight: 800;
                font-size: 18px !important;
                color: white;
                outline: none;
                background-color: rgb(10, 26, 51);
                border-radius: 0.5rem;
                border: 2px solid #2b3d58;
            }
            div[data-testid="stPageLink"] p:hover { 
                border: 2px solid #158fd8;
                box-shadow: 0 0 10px #158fd8;
            }
            div[data-testid="stPageLink"] p:active { 
                background-color: #192841;
            }</style>"""
    )
    st.divider()
    st.page_link("./all_pages/0 Home.py", label=_("Back to Home"))


def back_to_menu(selected_language):
    _ = set_localization(selected_language)

    def to_menu_page():
        st.session_state.page = "menu"

    st.html(
        """<style>
            div[data-testid="stAppViewBlockContainer"] div[data-testid="stButton"] button:nth-last-child(1) p::before { 
                font-family: "Font Awesome 5 Free" !important;
                content: "\\f0c9";
                display: inline-block;
                vertical-align: middle;
                font-weight: 900;
                font-size: 18px;
                color: white;
                padding-right: 8px;
            }
            div[data-testid="stAppViewBlockContainer"] div[data-testid="stButton"] button:nth-last-child(1) p { 
                font-weight: 900;
                font-size: 18px;
            }
            div[data-testid="stAppViewBlockContainer"] div[data-testid="stButton"] button[data-testid="baseButton-secondary"]:nth-last-child(1) { 
                position: absolute;
                right: 50%;
                transform: translateX(50%);
                padding: 5px 10px;
                border-radius: 0.5rem;
                border: 2px solid #2b3d58;
            }
            div[data-testid="stAppViewBlockContainer"] button[data-testid="baseButton-secondary"]:nth-last-child(1):hover { 
                border: 2px solid #158fd8;
                box-shadow: 0 0 10px #158fd8;
            }
            div[data-testid="stAppViewBlockContainer"] button[data-testid="baseButton-secondary"]:nth-last-child(1):active { 
                background-color: #192841;
            }</style>"""
    )
    st.divider()
    st.button(_("Back to Menu"), on_click=to_menu_page)


def common_config():
    st.set_page_config(
        page_title="WinterPixelGames » Tools and Stats",
        page_icon="static/wpg_hex_logo_144.png",
        layout="wide",
        initial_sidebar_state="auto",
    )

    st.logo(
        "static/streamlit_banner_v4.png",
        icon_image="static/wpg_hex_logo_144.png",
    )
    st.markdown(
        """
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@400..800&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"> 
        <style>
        *:hover {
            cursor: url('./app/static/cursor_v5.png'), auto !important;
        }
        *:focus {
            cursor: url('./app/static/cursor_v5.png'), auto !important;
        }
        body * {
            word-break: break-word;
        }
        a {
            text-decoration: none !important;
        }
        h1, h2, h3, h4, h5, h6, p, li, table, div[class="stHtml"] {
            font-family: 'Baloo 2' !important;
        }
        h3, h4 {
            font-weight: 800;
            font-size: 25px;
        }
        h3 {
            color: #32bafa;
        }
        h3, h4 {
            padding: 0;
        }
        section[data-testid="stSidebar"] {
            width: fit-content !important;
            padding-right: 3px !important;
            user-select: none !important;
        }
        div[data-testid="stSidebarNav"] > ul[data-testid="stSidebarNavItems"] > li > div > a > span {
            color: white !important;
            font-weight: 700;
            font-size: 25px;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(1) > div > a::before{
            font-family: "Font Awesome 5 Free" !important;
            content: "\\f015";
            display: inline-block;
            vertical-align: middle;
            font-weight: 800;
            font-size: 20px;
            color: white;
            min-width: 35px;
            padding-left: 8px;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(2) > div > a::before{
            content: "";
            background-image: url("./app/static/RocketBotRoyale/rocket_bot_royale_favicon.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 35px;
            width: 35px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(3) > div > a::before{
            content: "";
            background-image: url("./app/static/GooberDash/goober_dash_favicon.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 35px;
            width: 35px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(4) > div > a::before{
            content: "";
            background-image: url("./app/static/GooberRoyale/goober_royale_favicon.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 35px;
            width: 35px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(5) > div > a::before{
            content: "";
            background-image: url("./app/static/GooberShot/goober_shot_favicon.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 35px;
            width: 35px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(6) > div > a::before{
            content: "";
            background-image: url("./app/static/MoonrockMiners/moonrock_miners_favicon.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 35px;
            width: 35px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(7) > div > a::before{
            font-family: "Font Awesome 5 Free" !important;
            content: "\\f05a";
            display: inline-block;
            vertical-align: middle;
            font-weight: 800;
            font-size: 25px;
            color: white;
            min-width: 35px;
            padding-left: 6px;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(8) > div > a::before{
            font-family: "Font Awesome 5 Free" !important;
            content: "\\f08e";
            display: inline-block;
            vertical-align: middle;
            font-weight: 800;
            font-size: 20px;
            color: white;
            min-width: 35px;
            padding-left: 7px;
        }
        header {
            background: transparent !important;
        }
        button[data-baseweb="tab"] {
            color: #ffffff !important; 
        }
        div[data-baseweb="tab-list"] > div[data-baseweb="tab-highlight"] {
            background-color: #3097e6 !important;
        }
        div[data-testid="stSidebarHeader"] img[data-testid="stLogo"] {
            width: 100%;
            height: 100%;
            left: 12px;
            position: relative;
            transform: scale(1.2, 1.2);
            top: 15px;
        }
        div[data-testid="stDecoration"] {
            background-image: linear-gradient(90deg, rgb(0, 108, 176), rgb(0, 43, 71));
        }
        ul[data-testid="main-menu-list"] > ul:nth-child(4) {
            display: none;
        }
        ul[data-testid="main-menu-list"] > div[data-testid="main-menu-divider"] {
            display: none;
        } 
        body {
            overscroll-behavior-x: none !important;
            overscroll-behavior-y: none !important;
        }
        div[data-testid="collapsedControl"] {
            z-index: 9999999;
            left: 0.5rem;
        }
        div[data-testid="collapsedControl"] > div {
            padding-top: 8px;
            left: -3px;
            position: relative;
        }
        div[data-testid="stSidebarCollapseButton"] {
            position: relative;
            top: 25px;
            left: 25px;
        }
        div[data-testid="stSidebarCollapseButton"] > button[data-testid="baseButton-header"], button[data-testid="baseButton-headerNoPadding"] {
            border-radius: 50px;
        }
        div[data-testid="collapsedControl"] > button[data-testid="baseButton-headerNoPadding"] > svg {
            font-size: 1rem;
            position: relative;
        }
        * {
            cursor: url('./app/static/cursor_v5.png'), auto !important;
        }
        @supports not selector(::-webkit-scrollbar) {
            html {
                scrollbar-color: rgb(108, 195, 251) transparent !important;
            }
        }
        div[data-testid="stAppViewContainer"] ::-webkit-scrollbar {
            width: 6px !important;
        }
        div[data-testid="stAppViewContainer"] ::-webkit-scrollbar-track {
            background-color: rgba(255, 255, 255, 0.1) !important;
            border-radius: 6px !important;
            -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3) !important;
        }
        div[data-testid="stAppViewContainer"] ::-webkit-scrollbar-thumb {
            background-image: linear-gradient(45deg, rgba(22, 79, 122, 0.8), rgba(50, 144, 212, 0.8)) !important;
            border-radius: 6px !important;
            -webkit-box-shadow: rgba(0,0,0,.12) 0 3px 13px 1px !important;
        }
        div[data-testid="stAppViewContainer"] ::-webkit-scrollbar-thumb:hover {
            background-image: linear-gradient(45deg, rgba(22, 79, 122, 0.9), rgba(50, 144, 212, 0.9)) !important;
            border-radius: 6px !important;
            -webkit-box-shadow: rgba(0,0,0,.12) 0 3px 13px 1px !important;
        }
        div[data-testid="stAppViewContainer"] ::-webkit-scrollbar-thumb:active {
            background-image: linear-gradient(45deg, rgba(22, 79, 122, 1), rgba(50, 144, 212, 1)) !important;
            border-radius: 6px !important;
            -webkit-box-shadow: rgba(0,0,0,.12) 0 3px 13px 1px !important;
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            height: 33px;
            color: white;
            text-align: center;
            background-color: #081427;
            z-index: 99999;
            border-top: 1px solid #384251;
        }
        .footer > p {
            font-size: 0.7rem !important;
            line-height: 15px;
            margin-top: 2px;
        }
        div[data-testid="collapsedControl"] > div > button {
            margin: 0;
            position: relative;
            top: -2px;
            padding-left: 50px;
            left: -50px;
            transform: translateX(50px);
        }
        div[data-testid="collapsedControl"] button:hover {
            background-color: transparent;
        }
        div[data-testid="collapsedControl"]:hover {
            border-color: #158fd8;
            box-shadow: 0 0 12px #158fd8;
            transform: translateX(-10px);
            -webkit-transform:translateX(-10px);
            transition: 0.2s ease-in-out;
            -wenkit-transition: 0.2s ease-in-out;
            opacity: 1;
        }
        div[data-testid="collapsedControl"] {
            background: #192841;
            margin-left: -50px;
            left: -10px;
            padding: 3px 0 3px 30px;
            border: 1px solid #32bafa;
            border-radius: 50px;
            top: 35px;
            transform: translateX(-50px);
            opacity: 0.5;
        }
        div[data-testid="collapsedControl"] img {
            top: 6px;
            position: relative;
            left: -1px;
            transform: translateX(50px) scale(1.5,1.5);
        }
        div[data-testid="stAppViewBlockContainer"] p {
            font-size: 1.3rem;
        }
        hr:not([size]) {
            height: 1px;
            margin: 1rem 0px;
        }
        a[data-testid="baseLinkButton-primary"]:hover, a[data-testid="baseLinkButton-secondary"]:hover, div[data-testid="stVerticalBlock"] div:not([data-baseweb]) button:hover {
            color: white;
            outline: none;
            border: 1.5px solid #158fd8;
            box-shadow: 0 0 10px #158fd8;
        }
        a[data-testid="baseLinkButton-primary"]:focus, a[data-testid="baseLinkButton-secondary"]:focus, button:focus {
            color: white !important;
        }
        div[data-baseweb="tab-list"] button:hover {
            color: #158fd8 !important;    
            border: none !important;
            box-shadow: none !important;
        }
        section[data-testid="stSidebar"] > div:nth-child(2) > div > div {
            display: none;
        }
        div[data-testid="stAppViewBlockContainer"] {
            padding: 0px 5vw 100px 5vw !important;
        }
        div[data-testid="stNotification"] {
            padding: 10px;
        }
        div[data-testid="stSidebarContent"] {
            overflow: hidden;
        }
        div[data-testid="stAppViewBlockContainer"] div[data-testid="stFullScreenFrame"]:first-child > div {
            justify-content: center;
        }
        div[data-testid="stNotification"] {
            width: fit-content;
        }
        summary:hover {
            color: rgb(48, 151, 230) !important;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )


def footer_and_language(selected_language):
    _ = set_localization(selected_language)
    st.markdown(
        """
            <div class="footer">
            <p><span style="display:inline-block;">"""
        + _("This website is NOT affiliated with or endorsed by Winterpixel Games Inc.")
        + """</span><span style="display:inline-block;">&nbsp;"""
        + _("All relevant trademarks belong to their respective owners.")
        + """</span><br>"""
        + _(
            'Developed with 💖 by <a style="text-decoration:none" href="https://tank8k.com/" target="_blank">TANK8K</a>'
        )
        + """</p>
            <style>
            div[data-testid="stSidebarContent"] div[data-testid="stSelectbox"] label[data-testid="stWidgetLabel"]::before {
                content: '💬 """
        + _("Language")
        + """';
                font-family: 'Baloo 2';
                font-weight: 700;
                font-size: 20px;
            }
            </style>
        </div>
    """,
        unsafe_allow_html=True,
    )
