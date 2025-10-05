def bananabid(my_player_number, my_bananas, monkey_position, opponent_bananas, past_bid_list, turn_number):
	
	if turn_number == 1:
		return 32
	if opponent_bananas == 0
		return 1
	last_turn = past_bid_list[-1]
	opponent_bid = last_turn[2 - my_player_number]
	my_bid = last_turn[my_player_number]
	if my_bid <= opponent_bid 
		return opponent_bid/2 + 1
	
	else:
		return opponent_bid*2 + 1

