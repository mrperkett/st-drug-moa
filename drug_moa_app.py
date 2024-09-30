import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def main():

    st.markdown("# Drug Method of action")

    st.write("Placeholder application")

    cmap = st.selectbox("color map", ["rocket", "mako", "flare", "crest"])

    # placeholder: simple example of a clustermap
    iris = sns.load_dataset("iris")
    species = iris.pop("species")
    sns.clustermap(iris, cmap=cmap)
    fig = plt.gcf()

    st.pyplot(fig=fig)


if __name__ == "__main__":
    main()
