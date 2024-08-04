import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="A/B Testing",
        page_icon="🧪",
    )

    st.write("# Welcome! 👋")

    st.sidebar.success("Select a model choice above.")

    st.markdown(
        """
        This is a small app to test two models via A/B testing.

        **👈 Select a demo from the sidebar** to see two model types.
        
        🤔 Navigate over to the "Final Question" page to share your feedback on which is better!
    """
    )


if __name__ == "__main__":
    run()
