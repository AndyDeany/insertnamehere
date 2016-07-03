# Miscellaneous
if event.key == 8: backspace_held = 1
elif event.key == 9: tab_held = 1
elif event.key == 13: enter_held = 1
elif event.key == 19: pausebreak_held = 1
elif event.key == 27: escape_held = 1
elif event.key == 32: space_held = 1
elif event.key == 39: apostrophe_held = 1
elif event.key == 44: comma_held = 1
elif event.key == 45: minus_held = 1
elif event.key == 46: fullstop_held = 1
elif event.key == 47: forwardslash_held = 1
# Numbers across the top
elif event.key == 48: zero_held = 1
elif event.key == 49: one_held = 1
elif event.key == 50: two_held = 1
elif event.key == 51: three_held = 1
elif event.key == 52: four_held = 1
elif event.key == 53: five_held = 1
elif event.key == 54: six_held = 1
elif event.key == 55: seven_held = 1
elif event.key == 56: eight_held = 1
elif event.key == 57: nine_held = 1
# Miscellaneous
elif event.key == 59: semicolon_held = 1
elif event.key == 60: backslash_held = 1
elif event.key == 61: equals_held = 1
elif event.key == 91: opensquarebracket_held = 1
elif event.key == 92: sharp_held = 1
elif event.key == 93: closesquarebracket
elif event.key == 96: backtick_held = 1
# Alphabet
elif event.key == 97: a_held = 1
elif event.key == 98: b_held = 1
elif event.key == 99: c_held = 1
elif event.key == 100: d_held = 1
elif event.key == 101: e_held = 1
elif event.key == 102: f_held = 1
elif event.key == 103: g_held = 1
elif event.key == 104: h_held = 1
elif event.key == 105: i_held = 1
elif event.key == 106: j_held = 1
elif event.key == 107: k_held = 1
elif event.key == 108: l_held = 1
elif event.key == 109: m_held = 1
elif event.key == 110: n_held = 1
elif event.key == 111: o_held = 1
elif event.key == 112: p_held = 1
elif event.key == 113: q_held = 1
elif event.key == 114: r_held = 1
elif event.key == 115: s_held = 1
elif event.key == 116: t_held = 1
elif event.key == 117: u_held = 1
elif event.key == 118: v_held = 1
elif event.key == 119: w_held = 1
elif event.key == 120: x_held = 1
elif event.key == 121: y_held = 1
elif event.key == 122: z_held = 1
# Miscellaneous
elif event.key == 127: delete_held = 1
# Numpad
elif event.key == 256: numpad0_held = 1
elif event.key == 257: numpad1_held = 1
elif event.key == 258: numpad2_held = 1
elif event.key == 259: numpad3_held = 1
elif event.key == 260: numpad4_held = 1
elif event.key == 261: numpad5_held = 1
elif event.key == 262: numpad6_held = 1
elif event.key == 263: numpad7_held = 1
elif event.key == 264: numpad8_held = 1
elif event.key == 265: numpad9_held = 1
elif event.key == 266: numpaddivide_held = 1
elif event.key == 267: numpadmultiply_held = 1
elif event.key == 268: numpadminus_held = 1
elif event.key == 269: numpadplus_held = 1    
elif event.key == 270: numpadenter_held = 1
# Arrow keys
elif event.key == 273: uparrow_held = 1
elif event.key == 274: downarrow_held = 1
elif event.key == 275: rightarrow_held = 1
elif event.key == 276: leftarrow_held = 1
# Miscellaneous
elif event.key == 277: insert_held = 1
elif event.key == 278: home_held = 1
elif event.key == 279: end_held = 1
elif event.key == 280: pageup_held = 1
elif event.key == 281: pagedown_held = 1         
# F keys
elif event.key == 282: f1_held = 1
elif event.key == 283: f2_held = 1
elif event.key == 284: f3_held = 1
elif event.key == 285: f4_held = 1
elif event.key == 286: f5_held = 1
elif event.key == 287: f6_held = 1
elif event.key == 288: f7_held = 1
elif event.key == 289: f8_held = 1
elif event.key == 290: f9_held = 1
elif event.key == 291: f10_held = 1
elif event.key == 292: f11_held = 1
elif event.key == 293: f12_held = 1
# Temporary key modifiers
elif event.key == 303: rightshift_held = 1
elif event.key == 304: leftshift_held = 1
elif event.key == 305: rightcontrol_held = 1
elif event.key == 306: leftcontrol_held = 1
elif event.key == 308: alt_held = 1
#! shift_held = rightshift_held or leftshift_held       #! remove these or remove the separated ones above.
#! control_held = rightcontrol_held or leftcontrol_held #! if you keep these, you need to add recognition for them in keyup.py
#! Go through this at the end and decide if everything needs keeping. Especially if left/right shift/control need separate things at all.
