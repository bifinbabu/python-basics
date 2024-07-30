import re

text = "Elon musk's phone number is 9977998889, call him if you have any questions on dogecoin.Tesla's revenue is 40 billion Tesla's CFO number (999)-333-7777"

pattern = r"\(\d{3}\)-\d{3}-\d{4}|\d{10}"  # Usage of r

matches = re.findall(pattern, text)

print(matches)

# Double parenthesis approach instead of r

text = "Elon Musk's phone number is 9977998889, call him if you have any questions on Dogecoin. Tesla's revenue is 40 billion Tesla's CFO number (999)-333-7777"

pattern = "\\(\\d{3}\\)-\\d{3}-\\d{4}|\\d{10}"

matches = re.findall(pattern, text)

print(matches)

# Big text

text = '"Note 1 – Overview & Summary of Significant Accounting Policies \nOverview Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003 and converted to a Texas corporation on June 13, 2024. Unaudited Interim Financial Statements The consolidated financial statements, including the consolidated balance sheet as of June 30, 2024, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and six months ended June 30, 2024 and 2023, and the consolidated statements of cash flows for the six months ended June 30, 2024 and 2023, as well as other information disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2023 was derived from the audited consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2023. Note 2 – Fair Value of Financial Instruments \nASC 820, Fair Value Measurements (“ASC 820”) states that fair value is an exit price, representing the amount that would be received to sell an asset or paid to transfer a liability in an orderly transaction between market participants. As such, fair value is a market-based measurement that should be determined based on assumptions that market participants would use in pricing an asset or a liability. The three-tiered fair value hierarchy, which prioritizes which inputs should be used in measuring fair value, is comprised of: (Level I) observable inputs such as quoted prices in active markets; (Level II) inputs other than quoted prices in active markets that are observable either directly or indirectly and (Level III) unobservable inputs for which there is little or no market data. The fair value hierarchy requires the use of observable market data when available in determining fair value. Our assets and liabilities that were measured at fair value on a recurring basis were as follows (in millions):"'

pattern = r"Note \d – ([^\n]*)"

matches = re.findall(pattern, text)

print(matches)


text = "The gross operating cost least vehicle in FY2022 Q1 was in 4 billion, in the previous quarter ie, in FY2021 Q4 was 3 billion FY2021 Q5 fy2021 q3"

pattern = r"FY\d{4} (Q[1-4])"

matches = re.findall(pattern, text, re.IGNORECASE)

print(matches)

text = "The gross operating cost least vehicle in FY2022 Q1 was in $4.85 billion, in the previous quarter ie, in FY2021 Q4 was $3.2 billion"

# pattern = r"\$[0-9\.]+"
pattern = r"\$[\d\.]+"


matches = re.findall(pattern, text)

print(matches)
