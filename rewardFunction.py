
def reward_function(params):
    
    # Read input parameters
    
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    
    steering = abs(params['steering_angle']) 
    
    speed = params['speed']
    is_left_of_center = params['is_left_of_center']
    all_wheels_on_track = params['all_wheels_on_track']
    steps = params['steps']
    progress = params['progress']
    
    
    #setting reward to 0 inititially
    reward = 0.0
    
    ################ Reward based on location     ################ 
    # choosing to keep DeepRacer either in center or towards left of track - to be faster.

    if(is_left_of_center == True):
        reward *= 5.0
        
    else:
        reward -= 5.0


    ################ Rewards based on distance_from_center################
    # 1.0  -> at the center
    # 0.5  -> on track but at track_width/4 from center i.e. center of half of track
    # 1e-3 -> off track
    
    if(distance_from_center <= track_width / 2):
        reward += 1.0
    elif(distance_from_center <= track_width / 4):
        reward += 0.5
    else:
        reward -= 1e-3   #off track condition


    
    ################ Reward if the car pass every 100 steps faster than expected ################
    
    TOTAL_NUM_STEPS = 500

    if ((steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100) :
        reward += 10.0

    ################ Penality  ################
    # 1e-3 -> off track - wheels not on track
    # 2.2  -> slow
    # 3 -> all conditions meet - reward
    
    SPEED_THRESHOLD = 7.0

    if not all_wheels_on_track:
        reward -= 1e-3
    elif speed < SPEED_THRESHOLD:
        reward += 2.20 
    else:
        reward *= 3.0



    ################  Steering penality threshold  ################ 
    #threshold based on action space setting - selecting half of the steering capability
    ABS_STEERING_THRESHOLD = 15

    # Penalize reward if the car is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    return float(reward)
