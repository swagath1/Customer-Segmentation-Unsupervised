import streamlit as st
import pandas as pd
import pickle


# Load Models

with open('kmeans.pkl','rb') as f:
    kmeans = pickle.load(f)

with open('scaler.pkl','rb') as f:
    scaler = pickle.load(f)

with open('pca.pkl','rb') as f:
    pca = pickle.load(f)

with open('train_columns1.pkl','rb') as f:
    train_columns1 = pickle.load(f)


# Title

st.title("Customer Segmentation using Unsupervised Learning")

st.write(
"""
Predict the customer segment based on customer behaviour.
"""
)


# Inputs

price = st.number_input(
    "Price",
    min_value=0.0,
    value=200.0
)

time_spent_sec = st.number_input(
    "Time Spent (sec)",
    min_value=0,
    value=20
)

session_length = st.number_input(
    "Session Length",
    min_value=0,
    value=5
)

interaction_count = st.number_input(
    "Interaction Count",
    min_value=0,
    value=2
)


day = st.number_input(
    "Day",
    min_value=1,
    max_value=31,
    value=15
)

hour = st.number_input(
    "Hour",
    min_value=0,
    max_value=23,
    value=12
)

minute = st.number_input(
    "Minute",
    min_value=0,
    max_value=59,
    value=30
)


user_action = st.selectbox(
    "User Action",
    [
        'click',
        'drop',
        'purchase',
        'view',
        'wishlist'
    ]
)


category = st.selectbox(
    "Category",
    [
        'Electronics',
        'Fashion',
        'Groceries',
        'Home',
        'Beauty'
    ]
)


brand = st.text_input(
    "Brand",
    "Samsung"
)


channel = st.selectbox(
    "Channel",
    [
        'app',
        'mobile',
        'web'
    ]
)


device_type = st.selectbox(
    "Device Type",
    [
        'android',
        'desktop',
        'ios',
        'tablet'
    ]
)


region = st.selectbox(
    "Region",
    [
        'AU',
        'CA',
        'DE',
        'FR',
        'IN',
        'JP',
        'UK',
        'US'
    ]
)


traffic_source = st.selectbox(
    "Traffic Source",
    [
        'direct',
        'email',
        'organic',
        'paid_search',
        'referral',
        'social'
    ]
)



if st.button("Predict Customer Segment"):


    input_df = pd.DataFrame({

        'price':[price],

        'time_spent_sec':[time_spent_sec],

        'session_length':[session_length],

        'interaction_count':[interaction_count],

        'day':[day],

        'hour':[hour],

        'minute':[minute],

        'user_action':[user_action],

        'category':[category],

        'brand':[brand],

        'channel':[channel],

        'device_type':[device_type],

        'region':[region],

        'traffic_source':[traffic_source]

    })


    # Dummies

    input_df = pd.get_dummies(
        input_df,
        drop_first=True
    )


    # Match training columns

    input_df = input_df.reindex(
        columns=train_columns1,
        fill_value=0
    )


    # Remove clusters if present

    input_df = input_df.drop(
        columns=['clusters'],
        errors='ignore'
    )


    # Scale

    input_scaled = scaler.transform(input_df)


    # PCA

    input_pca = pca.transform(input_scaled)


    # Predict

    cluster = kmeans.predict(input_pca)[0]


    st.success(
        f"Predicted Cluster : {cluster}"
    )


    if cluster == 0:

        st.info(
        """
        Customer Type:

        Casual Visitors

        Recommendation:

        Improve engagement and provide discounts.
        """
        )



    elif cluster == 1:

        st.info(
        """
        Customer Type:

        Active Customers

        Recommendation:

        Personalized offers and loyalty rewards.
        """
        )



    elif cluster == 2:

        st.info(
        """
        Customer Type:

        Medium Value Customers

        Recommendation:

        Product recommendations and cross-selling.
        """
        )



    elif cluster == 3:

        st.info(
        """
        Customer Type:

        Core Customers

        Recommendation:

        Premium offers and loyalty programs.
        """
        )



    else:

        st.info(
        """
        Customer Type:

        Niche Customers

        Recommendation:

        Targeted marketing campaigns.
        """
        )