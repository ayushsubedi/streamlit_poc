"""Main module for the streamlit app"""
import streamlit as st
import pages.first, pages.second

PAGES = {
    "Home": pages.first,
    "Analysis1": pages.second,
    # "Analysis2": pages.third,
    # "Analysis3": pages.four,
}


def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    with st.spinner(f"Loading {selection} ..."):
        page.write()

    st.sidebar.title("Sth else")
    st.sidebar.info(
        """
        Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?
        """
    )
    st.sidebar.title("Sth else")
    st.sidebar.info(
        """
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.
        """
    )

if __name__ == "__main__":
    main()