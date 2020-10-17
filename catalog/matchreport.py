from catalog.models import PlayerModel, Rd1HoleModel, Rd1SlotModel, Rd1ScoreModel, Rd1StablefordModel, Rd2HoleModel, Rd2SlotModel, Rd2ScoreModel, Rd2StablefordModel, Rd3HoleModel, Rd3SlotModel, Rd3ScoreModel, Rd3StablefordModel, Rd4HoleModel, Rd4SlotModel, Rd4ScoreModel, Rd4StablefordModel, EventEntryModel, LeaderBoardModel, SportsTippingModel,SportsTippingResultsModel, SportsTippingScoreModel, Input_TourDetailsModel, AdminHoleDetails

#===create report if given round number===
def generate_round_variables(round_number):
    round_index = round_number - 1

#match round number to relevant model
    if round_number == 1:
        select_slot_model = Rd1SlotModel
        select_score_model = Rd1ScoreModel
        select_hole_model = Rd1HoleModel
    elif round_number == 2:
        select_slot_model = Rd2SlotModel
        select_score_model = Rd2ScoreModel
        select_hole_model = Rd2HoleModel
    elif round_number == 3:
        select_slot_model = Rd3SlotModel
        select_score_model = Rd3ScoreModel
        select_hole_model = Rd3HoleModel

#get players that have played in relevant round (played more than zero holes)
    round_details = select_slot_model.objects.filter(player_holesplayed__gt=0).order_by('-player_rankscore')

# CTP DETAILS
#Create list of CTP holes selected when creating round
    ctp_holes = []
    hole_details = select_hole_model.objects.filter(CTP__gt=0)
    for ctp in hole_details:
        ctp_holes.append(ctp.number)

#Create list of CTP holes in play in selected round
    ctp_details = select_score_model.objects.all()

    ctp_inplay = []
    for hole in ctp_details:
        ctp_inplay.append(hole.hole.number)

#Match winners to selected holes
    ctp_winners = []
    for hole in ctp_details:
        for ctp in ctp_holes:
            if hole.hole.number == ctp:
                try:
                    ctp_winners.append(select_score_model.objects.get(hole=hole.hole.number).ctp.name)
                except:
                    ctp_winners.append("no-one")

    zipped_ctp = list(zip(ctp_holes, ctp_winners))

# LD DETAILS
#Create list of LD holes selected when creating round
    ld_holes = []
    hole_details = select_hole_model.objects.filter(LD__gt=0)
    for ld in hole_details:
        ld_holes.append(ld.number)

#Create list of LD holes in play in selected round
    ld_details = select_score_model.objects.all()

    ld_inplay = []
    for hole in ld_details:
        ld_inplay.append(hole.hole.number)

#Match winners to selected holes
    ld_winners = []
    for hole in ld_details:
        for ld in ld_holes:
            if hole.hole.number == ld:
                try:
                    ld_winners.append(select_score_model.objects.get(hole=hole.hole.number).ld.name)
                except:
                    ld_winners.append("no-one")

    zipped_ld = list(zip(ld_holes, ld_winners))

# Get top 3 tussle scores
    tussle_results = select_slot_model.objects.filter(player_name__isnull=False).order_by('-tussle_score', 'player_score')

    if tussle_results != None:
        tussle_top3 = tussle_results[:3]

        tussle_names = []
        for tussler in tussle_top3:
            tussle_names.append(tussler.player_name.name)

        tussle_scores = []
        for tussler_score in tussle_top3:
            tussle_scores.append(tussler_score.tussle_score)

        zipped_tussle = list(zip(tussle_names, tussle_scores))
    else:
        zipped_tussle = []

# GET LEADERBOARD DETAILS
# Get ranked names, stbl, score
    ranked_names = []
    for player_name in round_details:
        ranked_names.append(player_name.player_name.name)
    print(ranked_names)

    ranked_stbl = []
    for player_stbl in round_details:
        ranked_stbl.append(player_stbl.player_stbl)
    print(ranked_stbl)

    ranked_strokes = []
    for player_strokes in round_details:
        ranked_strokes.append(player_strokes.player_score)
    print(ranked_strokes)

    zipped_round_results = list(zip(ranked_names, ranked_stbl, ranked_strokes))

    return zipped_round_results, zipped_ld, zipped_ctp, zipped_tussle, ranked_names, round_details, tussle_top3, round_index

#===Create golf results in zipped lists===
def get_golf_results(zipped_round_results, zipped_ctp, zipped_ld, zipped_tussle):
    # GOLF VARIABLES
    count_players = len(zipped_round_results)
    # ctp1_winner = zipped_ctp[0][1]
    # ctp1_hole = zipped_ctp[0][0]
    # ctp2_winner = zipped_ctp[1][1]
    # ctp2_hole = zipped_ctp[1][0]
    # ctp3_winner = zipped_ctp[2][1]
    # ctp3_hole = zipped_ctp[2][0]
    # # ctp4_winner = zipped_ctp[3][1]
    # # ctp4_hole = zipped_ctp[3][0]
    # ld1_winner = zipped_ld[0][1]
    # ld1_hole = zipped_ld[0][0]
    # # ld2_winner = zipped_ld[1][1]
    # # ld2_hole = zipped_ld[1][0]
    # tussle_winner = zipped_tussle[0][0]
    # tussle_win_stbl = zipped_tussle[0][1]
    # tussle_2nd = zipped_tussle[1][0]
    # tussle_3rd = zipped_tussle[2][0]

    return count_players, #ctp1_winner, ctp1_hole, ctp2_winner, ctp2_hole, ctp3_winner, ctp3_hole, ld1_winner, ld1_hole, tussle_winner, tussle_win_stbl, tussle_2nd, tussle_3rd

#create randomized lists NOTE: this might come from user input in final version
from catalog.models import MatchReportInput

import random
adjective1_list = ['saucy', 'sizzling', 'breathtaking']
adjective2_list = ['breathtaking', 'saucy', 'sizzling']
old_saying_list = ['Stone the Crows', 'Sweet Jesus', 'Cor blimey']
animals_list = ['cats', 'rhinos', 'giraffes']
fav_drink_list = ['Rosso di Montalcinos', 'tequilas', 'sparkling waters']
sports_expression_list = ['Always give it 110%', 'You miss 100% of the shots you don\'t take!', 'Full credit to the boys']
golf_saying_list = ['Drive for show, putt for dough', 'Got to be in it to win it', 'Gotta give it a chance!']
lyric_list = ["Baby you're a firework", "You gotta lose yourself in the music", "I'm a bat out of hell"]
group_noone_likes_list = ['frat bros', 'those dudes who drive loud motorcycles', 'Karens']
recent_news_event_list = ['the upcoming Presidential Election', 'the recent Supreme Court vacancy', 'the California wildfires']
jobs_list = ['accountants', 'lawyers', 'garbagemen']
office_perk_list = ['comfy chairs', 'free coffee', 'xbox']

#===Create descriptive details for report===
def get_descriptors(ranked_names, player_input, round_index):

    try:
        random_player1 = ranked_names[-1]
        random_player2 = ranked_names[-2]
    except:
        random_player1 = "No-one"
        random_player2 = "No-one"

    #enable generic
    if player_input == 'Auto':
        adjective1 = adjective1_list[round_index]
        adjective2 = adjective2_list[round_index]
        old_timey_expression = old_saying_list[round_index]
        animal_plural = animals_list[round_index]
        fav_drink = fav_drink_list[round_index]
        cliche_sports_expression = sports_expression_list[round_index]
        song_lyric = lyric_list[round_index]
        golf_expression = golf_saying_list[round_index]
        group_noone_likes = group_noone_likes_list[round_index]
        recent_news_event = recent_news_event_list[round_index]
        jobs = jobs_list[round_index]
        office_perk = office_perk_list[round_index]

    else:
    #dynamic variables
        player_select = MatchReportInput.objects.get(report_name__name=player_input)

        adjective1 = player_select.adjective1.lower()
        adjective2 = player_select.adjective2.lower()
        old_timey_expression = player_select.old_saying.capitalize()
        animal_plural = player_select.animals.lower()
        fav_drink = player_select.fav_drink.lower()
        cliche_sports_expression = player_select.sports_expression.capitalize()
        song_lyric = player_select.lyric.capitalize()
        golf_expression = player_select.golf_saying.capitalize()
        group_noone_likes = player_select.group_noone_likes.lower()
        recent_news_event = player_select.recent_news.lower()
        jobs = player_select.jobs.lower()
        #clean office perk to remove 'my' or 'the'
        office_perk_raw = player_select.office_perk.lower()
        if office_perk_raw.split()[0] in ['my', 'the', 'a']:
            office_perk = office_perk_raw.split(' ', 1)[1]
        else:
            office_perk = office_perk_raw

    return adjective1, adjective2, random_player1, old_timey_expression, animal_plural, fav_drink, random_player2, cliche_sports_expression, song_lyric, golf_expression, group_noone_likes, recent_news_event, jobs, office_perk

#===Write intro section of report===
def report_intro(round_number, round_index, random_player1, old_timey_expression, adjective1, fav_drink, animal_plural, group_noone_likes, recent_news_event, jobs, office_perk):
    #create round-specific phrases
    if round_number == 1:
        round_description = "What an exciting round to kick off proceedings for this storied Tour."
        pre_round_activity = "shanked another seven iron in pre-round warm-up"
    elif round_number == 2:
        round_description = "What an action-packed follow-up to yesterday's proceedings."
        pre_round_activity = "surreptitiously guzzled a pre-round transfusion"
    elif round_number == 3:
        round_description = "What an incredible finale to a spectacular few days."
        pre_round_activity = "reluctantly restocked about $100 worth of golf balls at the pro shop pre-round"
    else:
        round_description = "What a round!"
        pre_round_activity = "surveyed the scorecard"


    intro_descriptor_list = [
                            f'rumbled around out there like a group of {animal_plural} after one too many {fav_drink}',
                            f'were at each other’s throats like a bunch of {jobs} who’d just had their {office_perk} perks taken away',
                            f'got stuck into each other like a bunch of {group_noone_likes} arguing passionately about {recent_news_event}'
                            ]
    intro_descriptor = intro_descriptor_list[round_index]

    #write intro text
    intro_text = (
    f"Welcome to the match report for Round {round_number} of the Jersey Jaunt. \n\n\
    \
    {round_description} \n\n\
    \
    The play today could be summed up in one word: {adjective1}. \n\n\
    \
    As {random_player1} could be heard to say as he {pre_round_activity}:\
    '{old_timey_expression}, it’s going to be {adjective1} out there today'. \n\n\
    \
    And {adjective1} it was. From the first drive to the last putt, the players {intro_descriptor}. \n\n\
    "
    )

    return intro_text

#define ctp variables
def report_ctp(zipped_ctp, random_player2, golf_expression, round_index):

    num_ctps = len(zipped_ctp)

    #create long ctp descriptive text
    ctps_won = []
    for hole in zipped_ctp:
        if hole[1] != 'no-one':
            ctps_won.append(hole)
        else:
            pass

    ctp_descriptor_list = [
                            f'And just like in the animal kingdom, it didn’t take long for a dominant male to emerge. ',
                            f'And just like in the professional world, it didn’t take long for the cream to rise to the top. ',
                            f'But unlike the current news environment, it wasn’t long before some good news was on the horizon. '
                            ]
    ctp_descriptor = ctp_descriptor_list[round_index]

    if len(ctps_won) == 0:
        first_ctp_text = f'{ctp_descriptor}' + 'Although, this time, that wasn\'t going to be in the ctp competition, as no CTPs were awarded this round.'
        remaining_ctp_text = ""
    else:
        ctp1_winner = ctps_won[0][1]
        ctp1_hole = ctps_won[0][0]

        first_ctp_text = (
        f"{ctp_descriptor} \n\n\
        \
        This time, it was in the form of {ctp1_winner}, who drew first blood in the CTP on hole {ctp1_hole} with a shot so close that it caused \
        {random_player2} to spontaneously exclaim -- '{golf_expression}!' -- when he saw the ball sitting so close to the pin, much to the confusion of his playing partners. \n\n\
        "
        )

    #create list of remaining ctp winners
    if len(ctps_won) == 0:
        remaining_ctp_text = ""
    elif len(ctps_won) == 1:
        remaining_ctp_text = "And that was it for sharp-shooting, as, unfortunately for the touring group, no other CTPs were claimed this round."
    else:
        ctps_won.pop(0)
        ctps_list = []
        ctps_full_list = []
        for counter, grouping in enumerate(ctps_won):
            if len(ctps_won) == 1:
                ctps_list.extend([grouping[1], ", on hole ", str(grouping[0]), "."])
            elif counter < len(ctps_won)-1:
                ctps_list.extend([grouping[1], ", on hole ", str(grouping[0]), ","])
            else:
                ctps_list.extend([" and ", grouping[1], ", on hole ", str(grouping[0]), "."])
            ctps_details = "".join(ctps_list)
            ctps_full_list.append(ctps_details)
        ctps_full_details = " and ".join(ctps_full_list)
        remaining_ctp_text = "But that wasn't the end of the CTP points. Also getting on the board was " + ctps_details

    #define full ctp text
    ctp_text = first_ctp_text + remaining_ctp_text

    return ctp_text

#define ld variables
def report_ld(zipped_ld, song_lyric):

    num_lds = len(zipped_ld)

    #create long ld descriptive text
    lds_won = []
    for hole in zipped_ld:
        if hole[1] != 'no-one':
            lds_won.append(hole)
        else:
            pass

    if len(lds_won) == 0:
        first_ld_text = "\n\nMeanwhile, a different kind of dominance was supposed to be playing out in the longest drive competition. Unfortunately, however, that wasn't going to be the case this time, as no-one could convincingly lay claim to having a long D."
        remaining_ld_text = ""
    else:
        ld1_winner = lds_won[0][1]
        ld1_hole = lds_won[0][0]

        first_ld_text = (
            f"\n\nMeanwhile a different kind of dominance was also beginning to play out.\n\n\
            '{song_lyric}', said {ld1_winner} cryptically, as he strode across the tee box on hole {ld1_hole}. \n\n\
            But he soon made his meaning clear as he obliterated his drive up the fairway, claiming the first longest D, \
            and leaving the other players to quietly contemplate their relatively short Ds.\n\n"
            )

    #create list of remaining ld winners
    if len(lds_won) == 0:
        remaining_ld_text = ""
    elif len(lds_won) == 1:
        remaining_ld_text = "And, in fact, that would be it for D measuring this round, as unfortunately for the touring group, no other LDs were claimed."
    else:
        lds_won.pop(0)
        lds_list = []
        lds_full_list = []
        for counter, grouping in enumerate(lds_won):
            if len(lds_won) == 1:
                lds_list.extend([grouping[1], ", who claimed the points on hole ", str(grouping[0]), "."])
            elif counter < len(lds_won)-1:
                lds_list.extend([grouping[1], ", who claimed the points on hole ", str(grouping[0]), ","])
            else:
                lds_list.extend([" and ", grouping[1], ", who claimed the points on hole ", str(grouping[0]), "."])
            lds_details = "".join(lds_list)
            lds_full_list.append(lds_details)
        lds_full_details = " and ".join(lds_full_list)
        remaining_ld_text = "But that wasn't the end of the LD points. Also getting on the board was " + lds_details

    ld_text = first_ld_text + remaining_ld_text

    return ld_text

def report_tussle(zipped_tussle, cliche_sports_expression, round_index, adjective2):

    if len(zipped_tussle) != 0:
        tussle_winner = zipped_tussle[0][0]
        tussle_win_stbl = zipped_tussle[0][1]

        tussle_2nd = zipped_tussle[1][0]
        tussle_3rd = zipped_tussle[2][0]

        tussle_phrase_list = [
                            'And it was his adherence to those wise words that ultimately saw him claim victory, putting together ',
                            'Yet despite his trepidation, or perhaps because of it, it was he who emerged victorious, with ',
                            'And to everyone\'s surprise, that rousing pep talk turned out to make all the difference, inspiring '
                            ]
        tussle_variable_phrase = tussle_phrase_list[round_index]

        cliche_sports_expression_sentence = cliche_sports_expression[0].upper() + cliche_sports_expression[1:]

        tussle_text = (
        f"\n\nThings further heated up down the last stretch of the back nine as the players encountered the famous Snakepit Challenge. \n\n\
        '{cliche_sports_expression_sentence}', {tussle_winner} reminded himself as he contemplated the contest ahead. \
        \n\n{tussle_variable_phrase} \
        a {adjective2} performance that netted a stableford score of {tussle_win_stbl}, edging out {tussle_2nd} and {tussle_3rd}."
        )
    else:
        tussle_text = ""

    return tussle_text

def report_leaderboard(zipped_round_results, random_player1, round_number, adjective1):

    num_players = len(zipped_round_results)
    zipped_round_results.reverse()
    ordinal_nums = []
    for n in range(1,num_players+1):
        ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
        ordinal_nums.append(ordinal(n))

    leaderboard_intro_text = (
    f"\n\nAnd that brings us to the final leaderboard. \
    ")

    podium = 3
    #if statement if number of players is greater than podium number
    if num_players > podium:
        last_place_name = zipped_round_results[0][0]; last_place_points = zipped_round_results[0][1]; last_place_strokes = zipped_round_results[0][2]
        last_place_pos = ordinal_nums[num_players - 1]
        last_place_text = (
        f"\n\nRounding out the bottom we had {last_place_name}, who was unable to convert passion into points out there, finishing in {last_place_pos} place on {last_place_points} points."
        )
        #take out last-ranked player
        zipped_round_results.pop(0)
        #if statement if number of players is same as podium number
        if len(zipped_round_results) == podium:
            remaining_text = ""
        else:
            leaderboard_non_places = []
            leaderboard_full_list = []
            exclude_podium = len(zipped_round_results) - (podium + 1)
            #create list of add-on phrases for run-down of non-podium places
            commentary_phrases = [
            'found patches of inspiration out there but was unable to string enough of it together, to card ',
            'showed real grit and determination when the going got tough out there and managed to scrape together ',
            'threatened in parts, but ultimately failed to ignite, finishing with ',
            'rode his talent as far as it would take him, ultimately ending up with '
            'hit more good shots than bad and was unlucky to finish with ',
            'put in a very solid day\'s work out there, to record a business-like ',
            'showed glipses of brilliance and was unlucky to finish so far down a contested leaderboad, recording ',
            'hit an outstanding run of form, though not quite enough to take him all the way, ending with ',
            'played excellent golf for most of the day, with a few key moments letting him down, to score ',
            'demonstrated why he\'s considered such a threat in this tournament, shooting an impressive ',
            ]

            #loop through remaining players in results
            for counter, result in enumerate(zipped_round_results):
                #get ordinal position from ordinal_nums
                counter_calc = (len(ordinal_nums) - 2) - counter
                player_pos = ordinal_nums[counter_calc]
                #create list of component phrases for sentence
                leaderboard_non_places.extend(["\n\nIn ", player_pos, " place we had ", result[0], ", who "+str(commentary_phrases[counter]), str(result[1]), " points from ", str(result[2]), " shots."])
                if counter == exclude_podium:
                    break
            leaderboard_details = "".join(leaderboard_non_places)
            leaderboard_full_list.append(leaderboard_details)
            leaderboard_full_details = " ".join(leaderboard_full_list)

            remaining_text = leaderboard_full_details
        ##ADD PODIUM LOOPS HERE

    else:
        last_place_text = ""
        remaining_text = ""

    if num_players < podium:
        podium = num_players

    podium_intro_text = (
    f"\n\nAnd that brings us to the business end of the board, which was fiercely fought."
    )

    podium_list = zipped_round_results[-podium:]
    podium_places = []
    podium_full_list = []
    for counter, finish in enumerate(podium_list):
        podium_calc = podium - counter - 1
        podium_pos = ordinal_nums[podium_calc]
        if podium_pos == '1st':
            position_intro_text = "But refusing to be denied, and taking out the round, with a commanding display of tournament golf, in "
            round_descriptor = "put together a dominant performance to card "
            score_descriptor = "an outstanding "
        elif podium_pos == '2nd':
            position_intro_text = "Next up, grabbing the silver, and coming tantalisingly close to victory, in "
            round_descriptor = "was unlucky not to take out the win with "
            score_descriptor = "an excellent "
        else:
            position_intro_text = "Coming in "
            round_descriptor = "played consistently good golf where it counted, to amass "
            score_descriptor = "a very solid "

        podium_places.extend(["\n\n", position_intro_text, podium_pos, " place, we had ", finish[0], ", who ", round_descriptor, score_descriptor, str(finish[1]), " points from ", str(finish[2]), " shots."])
    podium_details = "".join(podium_places)
    podium_full_list.append(podium_details)
    podium_full_details = " ".join(podium_full_list)

    podium_text = podium_intro_text + podium_full_details

    conclusion_text = (
    f"\n\nAnd there we have it: Round {round_number} in the books, and at the end of the day, only one word could really sum it all up... {adjective1}."
    )

    leaderboard_text = leaderboard_intro_text + last_place_text + remaining_text + podium_text + conclusion_text

    return leaderboard_text


### AWS POLLY FUNCTIONS ####

#AWS Polly function to create audio file >3000 characters
def createReportLong(polly_client, voice, s3bucket, round_number, text):

    s3_prefix = 'MatchReport'+'-rd'+str(round_number)+'-'+str(voice)

    response = polly_client.start_speech_synthesis_task(
        Engine='neural', #polly and bucket region to must be us-east-1
        VoiceId=voice,
        OutputS3BucketName=s3bucket,
        OutputS3KeyPrefix=s3_prefix,
        OutputFormat='mp3',
        Text=text
        )

    taskId = response['SynthesisTask']['TaskId']

    s3_filename = s3_prefix +'.' + taskId + '.mp3'
    return s3_filename


#AWS Polly function to create audio file less than 3000 characters
def createReport(polly_client, text, round_number, voice):
    # Define Polly synthesize_speech request
    response = polly_client.synthesize_speech(
                    VoiceId=voice,
                    OutputFormat='mp3',
                    Text = text,
                    Engine='neural')

    #Create and save audio file
    filename = 'RoundReport-' + str(round_number) + '-' + voice
    file = open(filename, 'wb')
    file.write(response['AudioStream'].read())
    file.close()

    s3_filename = filename + '.mp3'

    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )
    try:
        response = s3_client.upload_file(filename, AWS_STORAGE_BUCKET_NAME, s3_filename)
    except ClientError as e:
        logging.error(e)
        return False

    return s3_filename
