def scandaroon_behaviour(initial_brashness, actions, echo_threshold):
    

    for actions in actions:
        if actions == "flap" or actions == "squawk":
            initial_brashness += 1
        elif actions == "rest" or actions == "peck":
            initial_brashness -= 1
            
    
    if initial_brashness >= echo_threshold:
        print("echo")
    else:
        print("no echo")
    


    

scandaroon_behaviour(10, ["flap", "flap"], 12)