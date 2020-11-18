def load_and_process(a):
    import pandas as pd
    import numpy as np
    df = pd.read_csv(a,sep=',',low_memory=False)
        # I am going to keeep the variables that I want for my analysis
    df.loc[df['pes19_turnout2019'] ==5, 'pes19_votechoice2019'] = 10 # I added those who did not vote to the vote choice variable
    df1 = df[['cps19_religion','cps19_province','cps19_yob','cps19_employment','cps19_gender','cps19_education','cps19_imm','cps19_bornin_canada','cps19_econ_retro','cps19_own_fin_retro','pes19_votechoice2019','pes19_nativism1','pes19_nativism5','pes19_immigjobs' ]]
        #### in this dataframe some of the missing variables are coded as a number. I want to change all those values to NAN so that I can drop them 

    df1.loc[df1['cps19_religion']==22, "cps19_religion"] = np.nan
    df1.loc[df1['cps19_religion']==23, "cps19_religion"] = np.nan
    df1.loc[df1['cps19_employment']==13, "cps19_employment"] = np.nan
    df1.loc[df1['cps19_education']==12, "cps19_education"] = np.nan
    df1.loc[df1['cps19_imm']==4, "cps19_imm"] = np.nan
    df1.loc[df1['cps19_econ_retro']==4, "cps19_econ_retro"] = np.nan
    df1.loc[df1['cps19_own_fin_retro']==4, "cps19_own_fin_retro"] = np.nan
    df1.loc[df1['pes19_votechoice2019']==7, "pes19_votechoice2019"] = np.nan
    df1.loc[df1['pes19_votechoice2019']==8, "pes19_votechoice2019"] = np.nan
    df1.loc[df1['pes19_votechoice2019']==9, "pes19_votechoice2019"] = np.nan
    df1.loc[df1['pes19_nativism1']==6, "pes19_nativism1"] = np.nan
    df1.loc[df1['pes19_nativism5']==6, "pes19_nativism5"] = np.nan
    df1.loc[df1['pes19_immigjobs']==6, "pes19_immigjobs"] = np.nan
    df1.loc[df1['cps19_bornin_canada']==3, "cps19_bornin_canada"] = np.nan

    df1= (df1.assign(age=lambda x:2019-x['cps19_yob']-1919)
          .dropna()
          .assign(cps19_religion=lambda x: x['cps19_religion'].astype('category'))
          .assign(cps19_province=lambda x: x['cps19_province'].astype('category'))
          .assign(cps19_employment=lambda x: x['cps19_employment'].astype('category'))
          .assign(cps19_gender=lambda x: x['cps19_gender'].astype('category'))
          .assign(cps19_education=lambda x: x['cps19_education'].astype('category'))
          .assign(cps19_imm=lambda x: x['cps19_imm'].astype('category'))
          .assign(cps19_bornin_canada=lambda x: x['cps19_bornin_canada'].astype('category'))
          .assign(pes19_votechoice2019=lambda x: x['pes19_votechoice2019'].astype('category'))
          .assign(pes19_nativism1=lambda x: x['pes19_nativism1'].astype('category'))
          .assign(pes19_nativism5=lambda x: x['pes19_nativism5'].astype('category'))
          .assign(pes19_immigjobs=lambda x: x['pes19_immigjobs'].astype('category'))
          .assign(cps19_econ_retro=lambda x: x['cps19_econ_retro'].astype('category'))
          .assign(cps19_own_fin_retro=lambda x: x['cps19_own_fin_retro'].astype('category'))
          .assign(cps19_religion= lambda x: x['cps19_religion'].map({1: 'Atheist', 2: 'Agnostic', 3: 'Buddhist', 4: 'Hindu', 5: 'Jewish', 6:'Muslim',7:'Sikh', 8:'Anglican', 9:'Baptist', 10: 'Catholic',11:'Orthodox', 12:'Jehovahs Witness', 13:'Lutheran', 14:'Church of Jesus Christ of the Latter Day Saints', 15:'Pentecostal/ Fundamentalist/ Born Again/ Evangelical', 16:'Presbyterian', 17:'Protestant', 18:'United Church of Canada', 19:'Christian Reformed', 20:'Salvation Army', 21:'Mennonite', 22:'Other'}))
          .assign(cps19_employment= lambda x:  x['cps19_employment'].map({1: 'Working for pay full-time', 2: 'Working for pay part-time', 3: 'Self employed', 4: 'Retired', 5: 'Unemployed/ looking for work', 6:'Student', 7: 'Caring for a family',8:'Disabled', 9:'Student and working for pay', 10: 'Caring for family and working for pay',11:'Retired and working for pay', 12:'Other'}))
          .assign(cps19_gender = lambda x:  x['cps19_gender'].map({1: 'Male', 2: 'Female', 3: 'Other'}))
          .assign(cps19_education = lambda x: x['cps19_education'].map({1: 'No schooling', 2: 'Some elementary school', 3: 'Completed elementary school', 4: 'Some secondary/ high school', 5: 'Completed secondary/ high school', 6:'Some technical', 7: 'Completed technical',8:'Some university', 9:'Bachelor degree', 10: 'Master degree',11:'Professional degree or doctorate'}))
          .assign(cps19_imm = lambda x: x['cps19_imm'].map({1: 'More immigrants', 2: 'Fewer immigrants', 3: 'About the same number of immigrants as now'}))
          .assign(cps19_bornin_canada = lambda x: x['cps19_bornin_canada'].map({1: 'Canadian', 2: 'Immigrant'}))
          .assign(pes19_nativism1 = lambda x: x['pes19_nativism1'].map({1: 'Strongly disagree', 2: 'Somewhat disagree', 3: 'Neither agree nor disagree', 4: 'Somewhat agree', 5: 'Strongly agree'}))
          .assign(pes19_nativism5 = lambda x: x['pes19_nativism5'].map({1: 'Strongly disagree', 2: 'Somewhat disagree', 3: 'Neither agree nor disagree', 4: 'Somewhat agree', 5: 'Strongly agree'}))
          .assign(pes19_immigjobs = lambda x: x['pes19_immigjobs'].map({1: 'Strongly disagree', 2: 'Somewhat disagree', 3: 'Neither agree nor disagree', 4: 'Somewhat agree', 5: 'Strongly agree'}))
          .assign(cps19_province = lambda x: x['cps19_province'].map( {14:'Alberta', 15:'British Columbia', 16:'Manitoba', 17:'New Brunswick', 18:'Newfoundland and Labrador', 19:'Northwest Territories', 20:'Nova Scotia', 21:'Nunavut', 22:'Ontario', 23:'Prince Edward Island', 24:'Quebec', 25:'Saskatchewan', 26:'Yukon'}))
          .assign(cps19_econ_retro = lambda x: x['cps19_econ_retro'].map({1: 'Got better', 2: 'Stayed about the same', 3: 'Got worse'}))
          .assign(pes19_votechoice2019= lambda x: x['pes19_votechoice2019'].map({1: 'Liberal', 2: 'Conservative', 3: 'NDP', 4: 'Bloc Québécois', 5: 'Green Party', 6:'People Party', 10: 'Not voted'}))
                    )
 
    return df1