import streamlit as st
from PIL import Image


from PIL import Image

def resize_image(image, new_width=480, new_height=360):
    """
    指定されたサイズに画像をリサイズする関数。
    Args:
    image (PIL.Image): リサイズする画像。
    new_width (int): リサイズ後の幅。デフォルトは480ピクセル。
    new_height (int): リサイズ後の高さ。デフォルトは360ピクセル。

    Returns:
    PIL.Image: リサイズされた画像。
    """
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Streamlitアプリケーションのタイトル
st.title('背景リサイザー')

# ファイルアップローダーの作成
uploaded_file = st.file_uploader("画像をアップロードしてください", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # 画像を読み込む
    image = Image.open(uploaded_file)
    st.image(image, caption='アップロードされた画像', use_column_width=True)

    # ドット絵に変換
    resize = resize_image(image)

    # 画像を表示
    st.image(resize, caption='変換後', use_column_width=True)

    # 画像を保存するオプション
    if st.button('画像を保存'):
        resize.save('resize.png')
        with open('resize.png', "rb") as file:
            btn = st.download_button(
            label='Download Image',
            data=file,
            file_name='resize_image.png',
            mime='image/png'
        )

