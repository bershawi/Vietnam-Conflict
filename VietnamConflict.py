import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Data
data = pd.read_csv('VietnamConflict.csv')
data1 = data[data['BRANCH'].isin(['ARMY','MARINE CORPS'])]
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 202)

# print(data1.head(5))
# print(data.columns)

#infantry troops
infantry_MOS = ['INFANTRY OPERATIONS AND INTELLIGENCE SPECIALIST', 'INDIRECT FIRE INFANTRYMAN', 'INFANTRY UNIT LEADER',
                'PARACHUTIST, INFANTRY UNIT COMMANDER', 'INFANTRYMAN', 'RIFLEMAN', 'MACHINEGUNNER',
                'INFANTRY OFFICER (I)', 'ASSAULTMAN', 'HEAVY ANTI-ARMOR WEAPONS INFANTRYMAN', 'MORTARMAN',
                'INFANTRY UNIT COMMANDER', 'BASIC INFANTRY OFFICER', 'RANGER, OPERATIONS AND TRAINING STAFF OFFICER (G3,A3,S3)',
                'INFANTRY SENIOR SERGEANT', 'BASIC INFANTRYMAN', 'RANGER, UNIT OFFICER, TRAINING CENTER',
                'RANGER, INFANTRY UNIT COMMANDER', 'RANGER', 'INFANTRY UNIT COMMANDER, (MECHANIZED)', 'LAV ASSAULTMAN',
                'SCOUT-SNIPER']

infantry=data1[data1['POSITION'].isin(infantry_MOS)]
infantry_cas = infantry.FATALITY_YEAR.count()
total_cas = data.FATALITY_YEAR.count()
infantry_portion = infantry_cas / total_cas * 100
# print('Infantrymen sustained {}% of total casualties in Vietnam war.'.format(infantry_portion))

#Non- Infantry
non_infantry = data1[-data1['POSITION'].isin(infantry_MOS)]
navy_af = data[data['BRANCH'].isin(['NAVY','AIR FORCE'])]
by_grade = ['E01', 'E02', 'E03', 'E04', 'E05', 'E06', 'E07', 'E08', 'E09', 'W01',
            'W02', 'W03','W04', 'W05', 'O01', 'O02', 'O03', 'O04', 'O05', 'O06', 'O07']
# plt.subplot(3,1,1)
# sns.countplot(x='PAY_GRADE',data=infantry,order=by_grade)
# plt.title('Infantry Casualties(ARMY & MARINE CORPS)')
# plt.xlabel('PAY GRADE')
# plt.ylabel('Number of Casualties')
# plt.subplot(3,1,2)
# sns.countplot(x='PAY_GRADE',data=non_infantry,order=by_grade)
# plt.title('Non-Infantry (ARMY & MARINE CORPS)')
# plt.xlabel('Pay Grade')
# plt.ylabel('Number Of Casualties')
# plt.subplot(3,1,3)
# sns.countplot(x='PAY_GRADE',data=navy_af,order=by_grade)
# plt.title('NAVY & AIR FORCE CASUALTIES')
# plt.xlabel('PAY GRADE')
# plt.ylabel('Number Of Casualties')
# plt.tight_layout()
# plt.show()


pd.options.mode.chained_assignment = None

#Infantry ages

birth = pd.Series(infantry.loc[:,'BIRTH_YEAR'].floordiv(10000),index=infantry.index)
infantry.loc[:,'BIRTH_YEAR'] = birth
for row in infantry:
    age_at_death = []
    birth = infantry.BIRTH_YEAR
    death = infantry.FATALITY_YEAR
    age = death - birth
    age_at_death.extend(age)
age = pd.Series(age_at_death,index=infantry.index)
infantry.loc[:,'AGE'] = age

#then non-infantry
birth = pd.Series(non_infantry.loc[:,'BIRTH_YEAR'].floordiv(10000),index=non_infantry.index)
non_infantry.loc[:,'BIRTH_YEAR'] = birth
for row in non_infantry:
    age_at_death2 = []
    birth = non_infantry.BIRTH_YEAR
    death = non_infantry.FATALITY_YEAR
    age = death - birth
    age_at_death2.extend(age)
age = pd.Series(age_at_death2,index=non_infantry.index)
non_infantry.loc[:,'AGE'] = age

#my sister service

birth = pd.Series(navy_af.loc[:,'BIRTH_YEAR'].floordiv(10000),index=navy_af)
navy_af.loc[:,'BIRTH_YR'] = birth
for row in navy_af :
    age_at_death3 = []
    birth = navy_af.BIRTH_YEAR
    death = navy_af.FATALITY_YEAR
    age = death - birth
    age_at_death3.extend(age)
age = pd.Series(age_at_death3,index=navy_af.index)
navy_af.loc[:,'AGE'] = age


# plt.subplot(3,1,1)
# sns.countplot(x='AGE',data= infantry)
# plt.title('Infantry Age at Death')
# plt.xlabel('Age')
# plt.ylabel('Number of Fatalities')
# plt.subplot(3,1,2)
# sns.countplot(x='AGE',data=non_infantry)
# plt.title('Non Infantry Age at death (ARMY & MARINE CORPS)')
# plt.xlabel('Age')
# plt.ylabel('Number of fatalities')
# plt.subplot(3,1,3)
# sns.countplot(x='AGE',data=navy_af)
# plt.title('Navy & Air Force Age at Death')
# plt.xlabel('AGE')
# plt.ylabel('Number Of Fatalities')
# plt.tight_layout()
# plt.show()


#Mean and Median

inf_mean = infantry.AGE.mean()
inf_median = infantry.AGE.median()
non_inf_mean = non_infantry.AGE.mean()
non_inf_median = non_infantry.AGE.median()
navy_mean = navy_af.AGE.mean()
navy_median = navy_af.AGE.median()
# print('Infantry mean and median age at death are '+ str(inf_mean) + 'and'+str(inf_median)+'respectively')
# print('AF/Navy mean and median age at death are '+ str(navy_mean) + 'and ' + str(navy_median) + 'respectively')

#Hostility

infantry['HOSTILITY_CONDITIONS'] = infantry['HOSTILITY_CONDITIONS'].replace(['H','HN'],['HOSTILE','NON-HOSTILE'])
# sns.countplot(x='HOSTILITY_CONDITIONS',data=infantry)
# plt.title('Casualty Breakdown, Infantry')
# plt.xlabel('HOSTILITY_CONDITIONS')
# plt.ylabel('Number Of Fatalities')
# plt.show()

total_deaths = infantry['HOSTILITY_CONDITIONS'].count()
hostile = infantry[infantry['HOSTILITY_CONDITIONS'] == ' Hostile']
hostile_death = hostile['HOSTILITY_CONDITIONS'].count()
non_hostile = infantry[infantry['HOSTILITY_CONDITIONS'] == 'Non_hostile']
non_hostile_death = non_hostile['HOSTILITY_CONDITIONS'].count()
non_hostile_ratio = non_hostile_death / total_deaths * 100
hostile_ratio = hostile_death / total_deaths * 100
    # print('Infantry Sms sustained {}% hostile casualties and {}% non-hostile casualties'.format(hostile_ratio,non_hostile_ratio))

