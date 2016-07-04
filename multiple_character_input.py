if frame % (fps/30) == 0:  # This means characters are written/deleted [30] times per second, which feels natural.
    if backspace_held_time > fps/2:
        input_text = input_text[:-1]
    elif (len(input_text) < maximum_characters and  # Checking if a key has been held for half a second or longer.
          max(space_held_time, apostrophe_held_time, comma_held_time, minus_held_time, fullstop_held_time,
              forwardslash_held_time, zero_held_time, one_held_time, two_held_time, three_held_time, four_held_time,
              five_held_time, six_held_time, seven_held_time, eight_held_time, nine_held_time, semicolon_held_time,
              backslash_held_time, equals_held_time, opensquarebracket_held_time, sharp_held_time,
              closesquarebracket_held_time, backtick_held_time, a_held_time, b_held_time, c_held_time, d_held_time,
              e_held_time, f_held_time, g_held_time, h_held_time, i_held_time, j_held_time, k_held_time, l_held_time,
              m_held_time, n_held_time, o_held_time, p_held_time, q_held_time, r_held_time, s_held_time, t_held_time,
              u_held_time, v_held_time, w_held_time, x_held_time, y_held_time, z_held_time, numpad0_held_time,
              numpad1_held_time, numpad2_held_time, numpad3_held_time, numpad4_held_time, numpad5_held_time,
              numpad6_held_time, numpad7_held_time, numpad8_held_time, numpad9_held_time, numpaddivide_held_time,
              numpadmultiply_held_time, numpadminus_held_time, numpadplus_held_time) > fps/2):
        keys = pygame.key.get_pressed()    
        if sum(map(return_key, character_keys)) == 1:    # Checking that only one key that provides a character input is currently pressed.
            input_text = "".join((input_text, input_text[-1]))