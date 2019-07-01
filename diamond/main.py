from diamond.classes import Subclass, LeftSubclass, RightSubclass, BaseClass

s = Subclass()
s.call_me()

print(s.num_sub_calls, s.num_left_calls, s.num_right_calls, s.num_base_calls)
