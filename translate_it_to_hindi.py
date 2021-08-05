def translate_it_to_hindi(model, input_sentence):
    predicted_word =''
    output_sentence =''
    seq    = tknizer_eng.texts_to_sequences([input_sentence])
    tokens = pad_sequences(seq, maxlen=40, dtype='int32', padding='post')
    initial_state = model.layers[0].initialize_states(1024)
    encoder_outputs, final_state_h, final_state_c = model.layers[0](tokens,initial_state)
    input  = np.array([[1]],dtype=np.int32)
    states = [final_state_h,final_state_c]
    while(predicted_word!='<end>'):
        decoder_output,decoder_state_h,decoder_state_c = model.layers[1](input, initial_states=states)
        output = model.layers[2](decoder_output)
        states = [decoder_state_h,decoder_state_c]
        output_word_index = np.argmax(output[0],axis=1)
        #print(output_word_index)
        #predicted_word = tknizer_hindi.index_word[output_word_index[0]]
        predicted_word = tknizer_hindi.index_word[output_word_index[0]]
        input = tknizer_hindi.word_index[predicted_word]
        input = np.array([[input]],dtype=np.int32)
        if (predicted_word!='<end>'):
            output_sentence+=predicted_word+" "
        else:
            output_sentence+=predicted_word
    return output_sentence
