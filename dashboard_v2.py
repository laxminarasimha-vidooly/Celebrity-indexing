# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 21:36:01 2020

@author: Acharya
"""

import os
os.chdir(r"F:\rerequiredstatscelebrityindexing\input")
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
#import plotly.express as px
#from flask import Markup
pd.set_option('display.max_colwidth', -1)

def norm(df):
    return (df-df.min())/(df.max()-df.min())

historical_affinity=pd.read_csv('historical_affinity.csv')
active_affinity=pd.read_csv('active_affinity.csv')
content_type_fb=pd.read_csv('content_type_fb.csv')
content_type_yt=pd.read_csv('content_type_yt.csv')
content_type_in=pd.read_csv('content_type_in.csv')
content_type_tw=pd.read_csv('content_type_tw.csv')
content_type_tk=pd.read_csv('content_type_tk.csv')
language_pref=pd.read_csv('langauge_pref.csv')
brand_mentions=pd.read_csv('brand_mention_wts.csv')
norm_mahadata=pd.read_csv('celebrity_indexing_sample.csv')
brand_mapping=pd.read_csv("historical_brand_mapping.csv")

for_model=norm_mahadata[:]

for_model.fillna(0, inplace=True)
for_model['celeb_age']=norm(1/for_model['celeb_age'])
for_model=for_model[['List of bollywood actors', 'YT_subscribers',
       'YT_views', 'YT_uploads', 'in_followers', 'in_uploads',
       'in_following', 'fb_followers', 'fb_uploads', 'fb_views',
       'tw_followers', 'tw_following', 'tk_diggs', 'tk_fans',
       'tk_following', 'tk_heart', 'tk_videos', 'tk_verified_status',
       'Gender of celebrity', 'Height of celebrity',
       'Weight of celebrity', 'geography of the celebrity',
       'geography of the celebrity_state', 'region of the celebrity',
       'DOD', 'YT_marker', 'FB_marker', 'TW_marker', 'TK_marker',
       'IN_marker', 'majority_lan_0', 'majority_lan_1', 'majority_lan_2',
       'majority_lan_3', 'minority_lan_0', 'minority_lan_1',
       'minority_lan_2', 'minority_lan_3', 'minority_lan_4',
       'minority_lan_5', 'minority_lan_6', 'minority_lan_7',
       'minority_lan_8', 'minority_lan_9', 'minority_lan_10',
       'minority_lan_11', 'minority_lan_12', 'minority_lan_13',
       'minority_lan_14', 'minority_lan_15', 'minority_lan_16',
       'minority_lan_17', 'Historical_associations_0',
       'Historical_associations_1', 'Historical_associations_2',
       'Historical_associations_3', 'Historical_associations_4',
       'Historical_associations_5', 'Historical_associations_6',
       'Historical_associations_7', 'Historical_associations_8',
       'Historical_associations_9', 'Historical_associations_10',
       'Historical_associations_11', 'Historical_associations_12',
       'Historical_associations_13', 'Historical_associations_14',
       'Historical_associations_15', 'Historical_associations_16',
       'Historical_associations_17', 'Historical_associations_18',
       'Historical_associations_19', 'Historical_associations_20',
       'Historical_associations_21', 'Historical_associations_22',
       'Historical_associations_23', 'Historical_associations_24',
       'Historical_associations_25', 'Historical_associations_26',
       'Historical_associations_27', 'Historical_associations_28',
       'Historical_associations_29', 'Historical_associations_30',
       'Historical_associations_31', 'Historical_associations_32',
       'Historical_associations_33', 'Historical_associations_34',
       'Historical_associations_35', 'Historical_associations_36',
       'Historical_associations_37', 'Historical_associations_38',
       'Historical_associations_39', 'Historical_associations_40',
       'Historical_associations_41', 'Historical_associations_42',
       'Historical_associations_43', 'Historical_associations_44',
       'Historical_associations_45', 'Historical_associations_46',
       'Historical_associations_47', 'Historical_associations_48',
       'Historical_associations_49', 'Historical_associations_50',
       'Historical_associations_51', 'Historical_associations_52',
       'Historical_associations_53', 'Historical_associations_54',
       'Historical_associations_55', 'Historical_associations_56',
       'Historical_associations_57', 'Historical_associations_58',
       'Historical_associations_59', 'Historical_associations_60',
       'Historical_associations_61', 'Historical_associations_62',
       'Historical_associations_63', 'Historical_associations_64',
       'Historical_associations_65', 'Historical_associations_66',
       'Historical_associations_67', 'Historical_associations_68',
       'Historical_associations_69', 'Historical_associations_70',
       'Active_endorsements_0', 'Active_endorsements_1',
       'Active_endorsements_2', 'Active_endorsements_3',
       'Active_endorsements_4', 'Active_endorsements_5',
       'Active_endorsements_6', 'Active_endorsements_7',
       'Active_endorsements_8', 'Active_endorsements_9',
       'Active_endorsements_10', 'Active_endorsements_11',
       'Active_endorsements_12', 'Active_endorsements_13',
       'upcoming_events_0', 'upcoming_events_1', 'upcoming_events_2',
       'upcoming_events_3', 'upcoming_events_4', 'upcoming_events_5',
       'upcoming_events_6', 'upcoming_events_7', 'content_type_YT_0',
       'content_type_YT_1', 'content_type_YT_2', 'content_type_YT_3',
       'content_type_YT_4', 'content_type_YT_5', 'content_type_YT_6',
       'content_type_TW_0', 'content_type_TW_1', 'content_type_TW_2',
       'content_type_TW_3', 'content_type_TW_4', 'content_type_FB_0',
       'content_type_FB_1', 'content_type_FB_2', 'content_type_FB_3',
       'content_type_FB_4', 'content_type_IN_0', 'content_type_IN_1',
       'content_type_IN_2', 'content_type_IN_3', 'content_type_IN_4',
       'content_type_IN_5', 'content_type_IN_6', 'content_type_TK_0',
       'content_type_TK_1', 'content_type_TK_2',
       'category_Historical_associations_0',
       'category_Historical_associations_1',
       'category_Historical_associations_2',
       'category_Historical_associations_3',
       'category_Historical_associations_4',
       'category_Historical_associations_5',
       'category_Historical_associations_6',
       'category_Historical_associations_7',
       'category_Historical_associations_8',
       'category_Historical_associations_9',
       'category_Historical_associations_10',
       'category_Historical_associations_11',
       'category_Historical_associations_12',
       'category_Historical_associations_13',
       'category_Historical_associations_14',
       'category_Historical_associations_15',
       'category_Historical_associations_16',
       'category_Historical_associations_17',
       'category_Historical_associations_18',
       'category_Historical_associations_19',
       'category_Historical_associations_20',
       'category_Historical_associations_21',
       'category_Historical_associations_22',
       'category_Historical_associations_23',
       'category_Historical_associations_24',
       'category_Historical_associations_25',
       'category_Historical_associations_26',
       'category_Historical_associations_27',
       'category_Historical_associations_28',
       'category_Historical_associations_29',
       'category_Historical_associations_30',
       'category_Historical_associations_31',
       'category_Historical_associations_32',
       'category_Historical_associations_33',
       'category_Historical_associations_34',
       'category_Historical_associations_35',
       'category_Historical_associations_36',
       'category_Historical_associations_37',
       'category_Historical_associations_38',
       'category_Historical_associations_39',
       'category_Historical_associations_40',
       'category_Historical_associations_41',
       'category_Historical_associations_42',
       'category_Historical_associations_43',
       'category_Historical_associations_44',
       'category_Historical_associations_45',
       'category_Historical_associations_46',
       'category_Historical_associations_47',
       'category_Historical_associations_48',
       'category_Historical_associations_49',
       'category_Historical_associations_50',
       'category_Historical_associations_51',
       'category_Historical_associations_52',
       'category_Historical_associations_53',
       'category_Historical_associations_54',
       'category_Historical_associations_55',
       'category_Historical_associations_56',
       'category_Historical_associations_57',
       'category_Historical_associations_58',
       'category_Historical_associations_59',
       'category_Historical_associations_60',
       'category_Historical_associations_61',
       'category_Historical_associations_62',
       'category_Historical_associations_63',
       'category_Historical_associations_64',
       'category_Historical_associations_65',
       'category_Historical_associations_66',
       'category_Historical_associations_67',
       'category_Historical_associations_68',
       'category_Historical_associations_69',
       'category_Historical_associations_70',
       'category_Active_endorsements_0', 'category_Active_endorsements_1',
       'category_Active_endorsements_2', 'category_Active_endorsements_3',
       'category_Active_endorsements_4', 'category_Active_endorsements_5',
       'category_Active_endorsements_6', 'category_Active_endorsements_7',
       'category_Active_endorsements_8', 'category_Active_endorsements_9',
       'category_Active_endorsements_10',
       'category_Active_endorsements_11',
       'category_Active_endorsements_12',
       'category_Active_endorsements_13', 'avg_videos_fb', 'fb_views_30',
       'fb_likes_30', 'fb_comments_30', 'fb_shares_30',
       'fb_video_duration_30', 'avg_videos_YT', 'YT_views_30',
       'YT_likes_30', 'YT_comments_30', 'YT_dislikes_30',
       'YT_video_duration_30', 'avg_videos_IN', 'IN_views_30',
       'IN_likes_30', 'IN_comments_30', 'IN_video_duration_30',
       'avg_videos_TK', 'TK_digg_30', 'TK_share_30', 'TK_comments_30',
       'TK_video_duration_30', 'YT_age', 'IN_age', 'fb_age', 'TK_age',
       'TW_age', 'celeb_age', 'Social_presence', 'avg_YT_subscribers',
       'avg_YT_views', 'avg_YT_uploads', 'avg_IN_followers',
       'avg_IN_uploads', 'avg_IN_following', 'avg_fb_followers',
       'avg_fb_uploads', 'avg_fb_views', 'avg_tw_followers',
       'avg_tw_following', 'avg_tk_diggs', 'avg_tk_fans',
       'avg_tk_following', 'avg_tk_heart', 'avg_tk_videos',
       'yt_views_uploads', 'yt_views_subscribers', 'in_followers_uploads',
       'in_following_uploads', 'fb_followers_uploads', 'fb_views_uploads',
       'tk_diggs_videos', 'tk_fans_videos', 'tk_following_videos',
       'tk_heart_videos', 'fb_views_videos_30', 'fb_likes_videos_30',
       'fb_comments_videos_30', 'fb_shares_videos_30', 'fb_eng_30',
       'fb_eng_video', 'YT_views_videos', 'YT_likes_videos',
       'YT_comments_videos', 'YT_dislikes_videos', 'YT_eng_30',
       'YT_eng_video', 'IN_views_video', 'IN_likes_video',
       'IN_comments_video', 'IN_eng_30', 'IN_eng_video', 'TK_views_video',
       'TK_likes_video', 'TK_comments_video', 'TK_eng_30', 'TK_eng_video',
       'no_of_his_brands', 'no_of_active_brands', 'no_of_upcomings',
       'Age_groups', 'sentiment_wt_fb', 'sentiment_wt_yt']]


def scoring(df, OldMax, OldMin, NewMax, NewMin):
    OldRange = (OldMax - OldMin)
#     if (OldRange == 0):
#         NewValue = NewMin
#     else:
    NewRange = (NewMax - NewMin)  
    NewValue = (((df - OldMin) * NewRange) / OldRange) + NewMin
    return NewValue

for_drop=['List of bollywood actors', 'tk_verified_status', 'Gender of celebrity',
          'geography of the celebrity', 'geography of the celebrity_state',
       'region of the celebrity', 'DOD', 'YT_marker', 'FB_marker',
       'TW_marker', 'TK_marker', 'IN_marker', 'majority_lan_0',
       'majority_lan_1', 'majority_lan_2', 'majority_lan_3',
       'minority_lan_0', 'minority_lan_1', 'minority_lan_2',
       'minority_lan_3', 'minority_lan_4', 'minority_lan_5',
       'minority_lan_6', 'minority_lan_7', 'minority_lan_8',
       'minority_lan_9', 'minority_lan_10', 'minority_lan_11',
       'minority_lan_12', 'minority_lan_13', 'minority_lan_14',
       'minority_lan_15', 'minority_lan_16', 'minority_lan_17',
       'Historical_associations_0', 'Historical_associations_1',
       'Historical_associations_2', 'Historical_associations_3',
       'Historical_associations_4', 'Historical_associations_5',
       'Historical_associations_6', 'Historical_associations_7',
       'Historical_associations_8', 'Historical_associations_9',
       'Historical_associations_10', 'Historical_associations_11',
       'Historical_associations_12', 'Historical_associations_13',
       'Historical_associations_14', 'Historical_associations_15',
       'Historical_associations_16', 'Historical_associations_17',
       'Historical_associations_18', 'Historical_associations_19',
       'Historical_associations_20', 'Historical_associations_21',
       'Historical_associations_22', 'Historical_associations_23',
       'Historical_associations_24', 'Historical_associations_25',
       'Historical_associations_26', 'Historical_associations_27',
       'Historical_associations_28', 'Historical_associations_29',
       'Historical_associations_30', 'Historical_associations_31',
       'Historical_associations_32', 'Historical_associations_33',
       'Historical_associations_34', 'Historical_associations_35',
       'Historical_associations_36', 'Historical_associations_37',
       'Historical_associations_38', 'Historical_associations_39',
       'Historical_associations_40', 'Historical_associations_41',
       'Historical_associations_42', 'Historical_associations_43',
       'Historical_associations_44', 'Historical_associations_45',
       'Historical_associations_46', 'Historical_associations_47',
       'Historical_associations_48', 'Historical_associations_49',
       'Historical_associations_50', 'Historical_associations_51',
       'Historical_associations_52', 'Historical_associations_53',
       'Historical_associations_54', 'Historical_associations_55',
       'Historical_associations_56', 'Historical_associations_57',
       'Historical_associations_58', 'Historical_associations_59',
       'Historical_associations_60', 'Historical_associations_61',
       'Historical_associations_62', 'Historical_associations_63',
       'Historical_associations_64', 'Historical_associations_65',
       'Historical_associations_66', 'Historical_associations_67',
       'Historical_associations_68', 'Historical_associations_69',
       'Historical_associations_70', 'Active_endorsements_0',
       'Active_endorsements_1', 'Active_endorsements_2',
       'Active_endorsements_3', 'Active_endorsements_4',
       'Active_endorsements_5', 'Active_endorsements_6',
       'Active_endorsements_7', 'Active_endorsements_8',
       'Active_endorsements_9', 'Active_endorsements_10',
       'Active_endorsements_11', 'Active_endorsements_12',
       'Active_endorsements_13', 'upcoming_events_0', 'upcoming_events_1',
       'upcoming_events_2', 'upcoming_events_3', 'upcoming_events_4',
       'upcoming_events_5', 'upcoming_events_6', 'upcoming_events_7',
       'content_type_YT_0', 'content_type_YT_1', 'content_type_YT_2',
       'content_type_YT_3', 'content_type_YT_4', 'content_type_YT_5',
       'content_type_YT_6', 'content_type_TW_0', 'content_type_TW_1',
       'content_type_TW_2', 'content_type_TW_3', 'content_type_TW_4',
       'content_type_FB_0', 'content_type_FB_1', 'content_type_FB_2',
       'content_type_FB_3', 'content_type_FB_4', 'content_type_IN_0',
       'content_type_IN_1', 'content_type_IN_2', 'content_type_IN_3',
       'content_type_IN_4', 'content_type_IN_5', 'content_type_IN_6',
       'content_type_TK_0', 'content_type_TK_1', 'content_type_TK_2',
       'category_Historical_associations_0',
       'category_Historical_associations_1',
       'category_Historical_associations_2',
       'category_Historical_associations_3',
       'category_Historical_associations_4',
       'category_Historical_associations_5',
       'category_Historical_associations_6',
       'category_Historical_associations_7',
       'category_Historical_associations_8',
       'category_Historical_associations_9',
       'category_Historical_associations_10',
       'category_Historical_associations_11',
       'category_Historical_associations_12',
       'category_Historical_associations_13',
       'category_Historical_associations_14',
       'category_Historical_associations_15',
       'category_Historical_associations_16',
       'category_Historical_associations_17',
       'category_Historical_associations_18',
       'category_Historical_associations_19',
       'category_Historical_associations_20',
       'category_Historical_associations_21',
       'category_Historical_associations_22',
       'category_Historical_associations_23',
       'category_Historical_associations_24',
       'category_Historical_associations_25',
       'category_Historical_associations_26',
       'category_Historical_associations_27',
       'category_Historical_associations_28',
       'category_Historical_associations_29',
       'category_Historical_associations_30',
       'category_Historical_associations_31',
       'category_Historical_associations_32',
       'category_Historical_associations_33',
       'category_Historical_associations_34',
       'category_Historical_associations_35',
       'category_Historical_associations_36',
       'category_Historical_associations_37',
       'category_Historical_associations_38',
       'category_Historical_associations_39',
       'category_Historical_associations_40',
       'category_Historical_associations_41',
       'category_Historical_associations_42',
       'category_Historical_associations_43',
       'category_Historical_associations_44',
       'category_Historical_associations_45',
       'category_Historical_associations_46',
       'category_Historical_associations_47',
       'category_Historical_associations_48',
       'category_Historical_associations_49',
       'category_Historical_associations_50',
       'category_Historical_associations_51',
       'category_Historical_associations_52',
       'category_Historical_associations_53',
       'category_Historical_associations_54',
       'category_Historical_associations_55',
       'category_Historical_associations_56',
       'category_Historical_associations_57',
       'category_Historical_associations_58',
       'category_Historical_associations_59',
       'category_Historical_associations_60',
       'category_Historical_associations_61',
       'category_Historical_associations_62',
       'category_Historical_associations_63',
       'category_Historical_associations_64',
       'category_Historical_associations_65',
       'category_Historical_associations_66',
       'category_Historical_associations_67',
       'category_Historical_associations_68',
       'category_Historical_associations_69',
       'category_Historical_associations_70',
       'category_Active_endorsements_0', 'category_Active_endorsements_1',
       'category_Active_endorsements_2', 'category_Active_endorsements_3',
       'category_Active_endorsements_4', 'category_Active_endorsements_5',
       'category_Active_endorsements_6', 'category_Active_endorsements_7',
       'category_Active_endorsements_8', 'category_Active_endorsements_9',
       'category_Active_endorsements_10',
       'category_Active_endorsements_11',
       'category_Active_endorsements_12',
       'category_Active_endorsements_13',
       'Age_groups']

old_score=(for_model.drop(for_drop, axis=1).sum(axis=1))/len(for_model.drop(for_drop,axis=1).columns.values)
new_score=scoring(old_score, np.max(old_score), np.min(old_score), 5, 1)

for_model['old_score']=old_score
for_model['new_score']=new_score

def celebrity_index(historical_affinity, active_affinity, content_type_fb, content_type_in,content_type_yt, content_type_tk, content_type_tw,brand_cat, language_pref, brand_mentions, gender=None, age_group=None, language=None):
    brand_wanted=['celeb_name', brand_cat]
    top_brand=pd.merge(historical_affinity[brand_wanted],active_affinity[brand_wanted], on='celeb_name', how='outer')
    top_brand=pd.merge(top_brand, content_type_fb[brand_wanted], on='celeb_name', how='outer')
    top_brand=pd.merge(top_brand, content_type_yt[brand_wanted], on='celeb_name', how='outer')
    top_brand=pd.merge(top_brand, content_type_in[brand_wanted], on='celeb_name', how='outer')
    top_brand=pd.merge(top_brand, content_type_tk[brand_wanted], on='celeb_name', how='outer')
    top_brand=pd.merge(top_brand, content_type_tw[brand_wanted], on='celeb_name', how='outer')    
    top_brand=pd.merge(top_brand, brand_mentions[brand_wanted], on='celeb_name', how='outer')
    
    top_brand.columns=['celeb_name', 'historical_brands', 'active_brands', 'con_fb', 'con_yt', 'con_in','con_tk', 'con_tw', 'brand_mentions']
    top_brand['Brand_affinity']=((top_brand['historical_brands']*0.3)+(top_brand['active_brands']*0.5)+(top_brand['con_fb']*0.04)+(top_brand['con_yt']*0.04)+(top_brand['con_in']*0.04)+(top_brand['con_tk']*0.04)+(top_brand['con_tw']*0.04)+(top_brand['brand_mentions'])*0.0)/7
    top_brand=top_brand[top_brand['Brand_affinity']!=0]
    top_brand['Brand_affinity_new']=scoring(top_brand['Brand_affinity'],np.max(top_brand['Brand_affinity']), np.min(top_brand['Brand_affinity']), 5,1)
    top_brand=(pd.merge(top_brand,for_model, right_on='List of bollywood actors', left_on='celeb_name', how='left')).drop('celeb_name', axis=1)
    
    print("language is {} \ngender is {} \nage group is {}".format(language, gender, age_group))
    if language!=None:    
        top_brand=(pd.merge(top_brand, language_pref[['celeb_name', language]], left_on='List of bollywood actors',right_on='celeb_name', how='outer')).drop('celeb_name',axis=1)    
        
        top_brand=top_brand[top_brand[language]!=0]
        top_brand=top_brand.sort_values(by=language, ascending=False)
    if gender!=None:
        top_brand=top_brand[top_brand['Gender of celebrity']==gender]
    if age_group!=None:
        top_brand=top_brand[top_brand['Age_groups']==age_group]

    top_brand['final_ranking']=(top_brand['new_score']+top_brand['Brand_affinity_new'])/10
    return top_brand.sort_values(['final_ranking'], ascending=[False])[:5]

app = Flask(__name__)

@app.route('/celebrity_indexing', methods=['GET', 'POST'])
def get_result():
    if request.method == 'POST':
#Brand_category="mobile"
#Gender=None
#Age_group=None
#Language=None 
        Brand_category = request.form.get('dvalue')
        Gender = request.form.get('dvalue1')
        Age_group= request.form.get('dvalue2')
        Language=request.form.get('dvalue3')
        print(Brand_category, Gender, Age_group, Language)
        
        if Language == " ":
            Language=None
        if Gender == " ":
            Gender=None
        if Age_group == " ":
            Age_group=None
        try:
            output=celebrity_index(historical_affinity, active_affinity, content_type_fb, content_type_in, content_type_yt, content_type_tk, content_type_tw,Brand_category,language_pref,brand_mentions, Gender, Age_group, Language)
            output.columns.values
            b=(output.drop(for_drop,axis=1).drop({'old_score', 'new_score','Brand_affinity', 'final_ranking', 'Height of celebrity', 'Weight of celebrity', 'historical_brands',
               'active_brands', 'con_fb', 'con_yt', 'con_in', 'con_tk', 'con_tw','brand_mentions', 'Brand_affinity_new'},axis=1))
            
            b.columns.values
            output['top_features']=''
            output.reset_index(inplace=True)
            for i in range(len(b)):
                c=np.array(b.iloc[i,:])
            #    print(c)
                indexes=c.argsort()[-5:][::-1]
                tops=[]
                
                for j in indexes:
                    tops.append(b.columns[j])
    #            print(tops)
                output.loc[i, 'top_features']=str(tops)
            
            branding=str(Brand_category)
            for x in range(len(output)):
                xxxx=norm_mahadata[norm_mahadata['List of bollywood actors']==str(output.loc[x,'List of bollywood actors'])]
                print(str(output.loc[x,'List of bollywood actors']))
                xxxx=xxxx[['List of bollywood actors',"Historical_associations_0","Historical_associations_1","Historical_associations_2","Historical_associations_3","Historical_associations_4","Historical_associations_5","Historical_associations_6","Historical_associations_7","Historical_associations_8","Historical_associations_9","Historical_associations_10","Historical_associations_11","Historical_associations_12","Historical_associations_13","Historical_associations_14","Historical_associations_15","Historical_associations_16","Historical_associations_17","Historical_associations_18","Historical_associations_19","Historical_associations_20","Historical_associations_21","Historical_associations_22","Historical_associations_23","Historical_associations_24","Historical_associations_25","Historical_associations_26","Historical_associations_27","Historical_associations_28","Historical_associations_29","Historical_associations_30","Historical_associations_31","Historical_associations_32","Historical_associations_33","Historical_associations_34","Historical_associations_35","Historical_associations_36","Historical_associations_37","Historical_associations_38","Historical_associations_39","Historical_associations_40","Historical_associations_41","Historical_associations_42","Historical_associations_43","Historical_associations_44","Historical_associations_45","Historical_associations_46","Historical_associations_47","Historical_associations_48","Historical_associations_49","Historical_associations_50","Historical_associations_51","Historical_associations_52","Historical_associations_53","Historical_associations_54","Historical_associations_55","Historical_associations_56","Historical_associations_57","Historical_associations_58","Historical_associations_59","Historical_associations_60","Historical_associations_61","Historical_associations_62","Historical_associations_63","Historical_associations_64","Historical_associations_65","Historical_associations_66","Historical_associations_67","Historical_associations_68","Historical_associations_69","Historical_associations_70","Active_endorsements_0","Active_endorsements_1","Active_endorsements_2","Active_endorsements_3","Active_endorsements_4","Active_endorsements_5","Active_endorsements_6","Active_endorsements_7","Active_endorsements_8","Active_endorsements_9","Active_endorsements_10","Active_endorsements_11","Active_endorsements_12","Active_endorsements_13"]]
                XX=brand_mapping[brand_mapping['Celeb_name']==str(output.loc[x,'List of bollywood actors'])]
                for column in XX.drop('Celeb_name',axis=1):
                    XX[column]=XX[column].str.lower()
                
                for y in range(len(XX)):
                    
                    brand_cat_presence=[ind for ind, x in enumerate(list(XX.iloc[y,:])) if x == branding]
                    brand_presence=[]
                    for i in range(len(brand_cat_presence)):
    #                    brand_presence=[]
                        brand_presence.append(xxxx.iloc[0,brand_cat_presence[i]])
                    print(brand_presence)
                    output.loc[x,'brands_in_active/history']=str(brand_presence)
    #        fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16], width=800, height=400)
    #        div = fig.to_html(full_html=False), div_placeholder=Markup(div)
            output=output[['List of bollywood actors','new_score','Brand_affinity_new', 'final_ranking', 'top_features', 'brands_in_active/history']]
            output.rename(columns={'List of bollywood actors':'Top_celebrities', 'new_score':'celebrity_social_score'}, inplace=True)
            print(output)
            output.dropna(subset=['Top_celebrities', 'celebrity_social_score', 'Brand_affinity_new', 'final_ranking', 'brands_in_active/history'],how='all',inplace=True)
            return render_template('web.html',  tables=[output.to_html(classes='data')], titles="")
        except Exception as e:
            print(e)
            output_error=pd.DataFrame()
            output_error.loc[0,'message']=str('no data available in the specified category')
            print(output_error)
            return render_template('web.html',  tables=[output_error.to_html(classes='data')], titles="")
            print(output)


    html_body='''
    <!doctype html>
    <style>
    body, html {
      width: 99.5%;
      height: 95%;
      margin: 5px;
    }
    
    .container {
      width: 100%;
      height: 100%;
    }
    
    .middlepane {
    	text-align: center;
        width: 100%;
        height: 100%;
    	float: left;
        border-collapse: collapse;
    	display: inline;
        margin-start: auto;
        margin-end: auto;
        overflow: hidden;
        border-style: groove;
        border-width: 2.5px;
    }
    
    .toppane {
      width: 100%;
      height: 40px;
      border-collapse: collapse;
      background-color: #FF0000;
      text-align: center;
    }
    </style>
    
    <head>
     <div class="container">
    	<div class="toppane"><h1>Celebrity Indexing</h1></div>
        
        <form method=post enctype=multipart/form-data>
    	<div class="middlepane"><p><font size="4">Brand Category
            
            <select name= "dvalue" method="GET">
                
				<option value= "telecom">Telecom </option>
				<option value= "fmcg">FMCG </option>
				<option value= "e-commerce">E-Commerce </option>
				<option value= "consumer durables">Consumer Durables </option>
				<option value= "food & beverage">Food & Beverage </option>
				<option value= "health industry">Health Industry </option>
				<option value= "travel/tourism">Travel/Tourism </option>
				<option value= "automotive">Automotive </option>
				<option value= "building & industrial material">Building & Industrial Material </option>
				<option value= "bfsi">BFSI </option>
				<option value= "apparel | fashion | accessories">Apparel | Fashion | Accessories </option>
				<option value= "real estate">Real Estate </option>
				<option value= "sports">Sports </option>
				<option value= "it services">IT Services </option>
				<option value= "heavy machinery">Heavy Machinery </option>
				<option value= "conglomerate">Conglomerate </option>
				<option value= "media,event & advertising">Media,Event & Advertising </option>
				<option value= "satellite tv">Satellite TV </option>
				<option value= "education">Education </option>
				<option value= "medical/pharma industry">Medical/Pharma Industry </option>
				<option value= "hospitality">Hospitality </option>
				<option value= "aviation">Aviation </option>
				<option value= "retail">Retail </option>
				<option value= "consulting">Consulting </option>
				<option value= "energy/petroleum">Energy/Petroleum </option>
				<option value= "gaming">Gaming </option>
				<option value= "handicraft">Handicraft </option>
				<option value= "music">Music </option>
				<option value= "wildlife photography">Wildlife Photography </option>
				<option value= "alcohol and tobacco">Alcohol and Tobacco </option>
				<option value= "ngo">NGO </option>
				<option value= "social awareness">Social awareness </option>
				<option value= "services">Services </option>
				<option value= "mobile">Mobile </option>
				<option value= "mobile apps">Mobile Apps </option>
			</select>
          <p><div class="form-group">
			<div class="middlepane"><p><font size="4">Gender of celebrity
            <select name= "dvalue1" method="GET">
    			<option value= " "> </option>	
                <option value= "male">Male </option>
				<option value= "female">Female </option>
            </select>
			<p><div class="form-group">
            <div class="middlepane"><p><font size="4">Age group of celebrity
            <select name= "dvalue2" method="GET">
                <option value= " "> </option>
				<option value= "Kids">Kids(0-12) </option>
				<option value= "Adolescents">Adolescents(12-18) </option>
				<option value= "Adults">Adults(18-40) </option>
				<option value= "Middle_aged">Middle-aged(40-60) </option>
				<option value= "Seniors">Seniors(>60) </option>
            </select>
            <p><div class="form-group">
            <div class="middlepane"><p><font size="4">Language preference
            <select name= "dvalue3" method="GET">
                <option value= " "> </option>
				<option value= "assamese">Assamese </option>
				<option value= "bengali">Bengali </option>
				<option value= "bhojpuri">Bhojpuri </option>
				<option value= "chhattisgarhi">Chhattisgarhi</option>
                <option value= "english">English</option>
				<option value= "gujarati">Gujarati </option>
				<option value= "hindi">Hindi</option>
				<option value= "kannada">Kannada</option>
				<option value= "konkani">Konkani</option>
				<option value= "maithili">Maithili</option>
				<option value= "malayalam">Malayalam</option>
				<option value= "manipuri">Manipuri</option>
				<option value= "marathi">Marathi</option>
				<option value= "odia">Odia</option>
				<option value= "punjabi">Punjabi</option>
				<option value= "tamil">Tamil</option>
				<option value= "telugu">Telugu</option>
				<option value= "tulu">Tulu</option>
				<option value= "urdu">Urdu</option>
          </div>
          <p> <input type="submit" name="submit_button" value="Submit" onclick="return confirm('Do you want to submit?')" /></div>
        </form>
    '''
    return html_body

   
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)