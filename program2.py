def decode_message(message: str, decoder_key: str) -> bool:
    m, n = len(message), len(decoder_key)
    # dp[i][j] means whether message[0:i] matches decoder_key[0:j]
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # Handle cases where decoder_key contains leading '*'
    for j in range(1, n + 1):
        if decoder_key[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if decoder_key[j - 1] == '*':
                # '*' can match an empty sequence or one more character from the message
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif decoder_key[j - 1] == '?' or decoder_key[j - 1] == message[i - 1]:
                # '?' matches a single character or characters match exactly
                dp[i][j] = dp[i - 1][j - 1]
    
    return dp[m][n]
