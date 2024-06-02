import streamlit as st
from common_config import common_config, back_to_home

common_config()

st.html(
    """
    <style>
        div[data-testid="column"] {
            width: fit-content !important;
            flex: unset;
        }
        div[data-testid="column"] * {
            width: fit-content !important;
        }
        a[data-testid="baseLinkButton-secondary"] {
            border: 2px solid #2b3d58;
        }
        a[data-testid="baseLinkButton-secondary"]:hover {
            border: 2px solid #158fd8
        }
        div[data-testid="stLinkButton"] p {
            font-weight: 800;
        }
        div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(5) > div:nth-child(1) p::before {
            background-image: url("./app/static/rocket_bot_royale_favicon.png");
        }
        div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(5) > div:nth-child(2) p::before {
            background-image: url("./app/static/goober_dash_favicon.png");
        }
        div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(5) > div:nth-child(3) p::before {
            background-image: url("./app/static/goober_royale_favicon.png");
        }
        div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(5) > div:nth-child(4) p::before {
            background-image: url("./app/static/goober_shot_favicon.png");
        }
        div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(5) > div:nth-child(5) p::before {
            background-image: url("./app/static/moonrock_miners_favicon.png");
        }
        div[data-testid="stVerticalBlock"] div:nth-child(10) > div p::before {
            background-image: url("./app/static/wph_logo.png");
        }
        div[data-testid="stVerticalBlock"] div:nth-child(10) > div p::before, div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(5) > div p::before {
            content: "";
            background-size: 100% 100%;
            display: inline-block;
            vertical-align: middle;
            height: 35px;
            width: 35px;
            margin-right: 8px;
        }
        div[data-testid="stVerticalBlock"] div:nth-child(14) p:nth-child(2) {
            position: relative;
            top: -15px;
        }
        div[data-testid="stAppViewBlockContainer"] {
            padding: 50px 5vw 100px 5vw !important;
        }
        h4 {
            padding-bottom: 15px;
        }
        h3 {
            padding-bottom: 0;
        }
    </style>
    """
)

st.html(
    """
    <h4><i class="fa-solid fa-arrow-up-right-from-square" style="display: inline; margin: 0 5px 8px 0; width: 25px"></i>Useful Links</h4><h3><span style="font-size: 25px;">Staging Servers<span></h3>
    """
)

st.markdown(
    """**Staging Servers** are seperate servers which are used for testing new features before releasing. Usually updates are released on **Staging Servers** a few days before public release. Developers invite members to test out some upcoming features and ask for feedbacks in **Offcial Winterpixel Games Discord server** occasionally.
"""
)

col1, col2, col3, col4, col5 = st.columns(5)
col1.link_button("Rocket Bot Royale", "https://staging-rocketbotroyale.winterpixel.io/")
col2.link_button("Goober Dash", "https://upguys-staging.winterpixel.io/")
col3.link_button(
    "Goober Royale",
    "https://gooberroyale-staging.winterpixel.io/",
)
col4.link_button("Goober Shot", "https://gooberfall-staging.winterpixel.io/")
col5.link_button("Moonrock Miners", "https://staging-asteroids.winterpixel.io/")

st.error(
    "**Staging Servers** use seperate databases. **DO NOT** spend money on **Staging Server** as items cannot be transferred.",
    icon="🚨",
)

"---"

st.html(
    """
    <h3><span style="font-size: 25px;">Friendly Websites<span></h3>
    """
)

st.markdown(
    """[**WinterPixel Helper** (WpH)](https://wph.ambersys.app/) is a community-driven site made by [**thehermit**](https://ambersys.app/) which provides useful **Scripts** of games made by **[Winterpixel Games](https://www.winterpixel.com/)**, including **[Rocket Bot Royale](./Rocket_Bot_Royale)**, **[Goober Dash](./Goober_Dash)**, **[Goober Royale](./Goober_Royale)**.
"""
)

st.link_button("WinterPixel Helper", "https://wph.ambersys.app/")

st.warning(
    "The scripts in **WinterPixel Helper** should **NOT** be discussed on the **Official Winterpixel Games Discord server** as Moderators **DO NOT APPROVE** promoting non-official tools and scripts. Member who breaks the rules may result in a ban. However, you can enlighten people to this project through DMs and the such.",
    icon="⚠️",
)
back_to_home()
