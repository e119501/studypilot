from otree.api import *
# from jinja2 import Template, Environment, FileSystemLoader
 

doc = """Big 5 personality test"""

def make_q(label):
    return models.IntegerField(label=label, choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelect)


    #q1 = make_q('賃金を重視')
    #q2 = make_q('終身雇用')
    #q1 = make_q('賃金を重視')
    #q2 = make_q('終身雇用')
    #q1 = make_q('賃金を重視')
    

class Constants(BaseConstants):
    name_in_url = 'bigfive'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_q(label):
    return models.IntegerField(label=label, choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelect)

def make_p(label):
    return models.IntegerField(label=label, choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelect)

def make_a(label):
    return models.IntegerField(label=label, choices=[1, 2, 3, 4, 5,6,7,8,
    9,10,11,12,13], widget=widgets.RadioSelect)

def make_b(label):
    return models.IntegerField(label=label, choices=[1, 2], widget=widgets.RadioSelect)

def make_c(label):
    return models.IntegerField(label=label, choices=[1, 2, 3], widget=widgets.RadioSelect)

class Player(BasePlayer):
    q1 = make_c('性別')
    q2 = make_b('学年')
    q3 = make_b('文理')
    q4 = make_a('第一志望') 
    q5 = make_a('第二志望')
    q6 = make_a('第三志望')
    q7 = make_q('高賃金であること')
    q8 = make_q('終身雇用制度')
    q9 = make_q('福利厚生が充実していること')
    q10 = make_q('社風が自分に合っている（働きやすい）こと')
    q11 = make_q('やりがいのある仕事であること')
    q12 = make_q('自分の強みを生かせる仕事であること')
    q13 = make_q('自分が成長できるかどうか')
    q14 = make_q('企業理念に共感できる')
    q15 = make_q('環境に配慮した企業活動をしていること（植林なども含む）')
    q16 = make_q('雇用の機会均等を実現していること')
    q17 = make_q('貧困や飢餓をなくすための取り組みを行っていること')
    q18 = make_q('法令順守やコンプライアンスの意識が高いこと')
    q19 =  make_p('変わり目')
    q20 =  make_p('変わり目')
    
   

    外的報酬 = models.FloatField()
    内的報酬 = models.FloatField()
    社会的貢献 = models.FloatField()
    合計値 = models.FloatField()
    判定 = models.StringField()
    選好先攻 = models.FloatField()
    選好後攻 = models.FloatField()
    結果 =  models.StringField()
    #neuroticism = models.FloatField()
    #openness = models.FloatField()


def combine_score(a, b, c, d):
    return a+ b+ c +d

def combine_score2(a, b, c):
    return a+ b+ c

# def judge_score(): 
#     if player.q11 == "1.0":
#         return player.結果 == '競争的'
#     else:
#         return player.結果 == '非競争的'

class Honehone(Page):
    pass

class index(Page):
    form_model = 'player'
    form_fields = ['q1','q2','q3']

class Jamoji(Page):
    form_model = 'player'
    form_fields = ['q4', 'q5', 'q6']


class Survey(Page):
    form_model = 'player'
    form_fields = ['q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18']
    
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.外的報酬 = combine_score(player.q7, player.q8, player.q9, player.q10)
        player.内的報酬 = combine_score(player.q11, player.q12, player.q13, player.q14)
        player.社会的貢献 = combine_score(player.q15, player.q16, player.q17, player.q18)
        

        player.合計値 = combine_score2(player.外的報酬, player.内的報酬, player.社会的貢献 )
        player.判定 = 'ちょうど３０点にしてね'
        


class Results(Page):
    pass



class Baikin(Page):
    form_model = 'player'
    form_fields = ['q19']
    
    def before_next_page(player: Player, timeout_happened):
        player.選好先攻 = player.q11

    
   


# def judge_score(): 
#     if player.選好先攻 == "1.0":
#         return player.result == '競争的'
#     else:
#         return player.result == '非競争的'
    
   




class Dokin(Page):
    form_model = 'player'
    form_fields = ['q20']
    
    def before_next_page(player: Player, timeout_happened):
        player.選好後攻 = player.q12
    
        




        
        




      
#@staticmethod
#def message(player: Player):
 #       if player.合計値 > 30:
  #          player.判定 == '多いよ'
   #     elif player.合計値 < 30:
    #        player.判定 ==  '少ないよ'
     #   else:
      #      player.判定 ==  'ぴったり'
        




class Resultss(Page):
    pass
    # @staticmethod
    # def before_next_page(player: Player, timeout_happened):
    #     judge_score()







class Last(Page):
    pass

page_sequence = [Honehone, index, Jamoji, Survey, Results, Baikin, Dokin, Resultss, Last]