# Solar panels detector

This repo accompanies [the serving part of the blogposts series on Solar Panel detection](https://appsilon.com/using-streamlit-to-deploy-poc-app-part-3/).

## Remarks

This is a dead simple way of serving your models with `streamlit`.
Take it just as an inspiration and take the following things into consideration when deploying your model with `streamlit`:

1. To make app multiple user-friendly leverage [temporary files](https://docs.python.org/3/library/tempfile.html) in python.
2. Use functions in general
3. Use [caching mechanisms](https://docs.streamlit.io/library/api-reference/performance/st.experimental_singleton) of `streamlit`.
4. [Serialize your ML models](https://appsilon.com/model-serialization-in-machine-learning/) for production.
5. ...

