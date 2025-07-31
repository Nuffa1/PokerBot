from collections import namedtuple
from math import random
import streamlit as st
initial_balance = 100000
balance = initial_balance
betting_style = 'flat'  # Options: 'flat', 'martingale', 'anti-martingale'
minimum_bet = 10
players = ['Player1', 'Player2', 'Player3']  # List of players
if(balance < minimum_bet):
    raise ValueError("Insufficient balance to place a bet.")
total_cards = 52
cards_in_hand = 2
river_cards = 3
river = [Card(random(A,2,3,4,5,6,7,8,9,10,J,Q,K), random('hearts', 'diamonds', 'clubs', 'spades')) for _ in range(river_cards)]



Card = namedtuple('Card', ['rank', 'suit'])


card = Card('A', 'spades')
hand = [Card(st.text_input(placeholder="Enter rank (e.g., A, 2, ..., K)"),st.text_input(placeholder="Enter suit (e.g., hearts, diamonds, clubs, spades)"))]

print(card.rank, card.suit) 

