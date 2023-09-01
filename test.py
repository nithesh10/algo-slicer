if(int(df1["FNF"]["Force Sell"][0])==1):
    sym,token=gettokenid("FINNIFTY",df1['FNF']['EXS EXP SELL'],df1['FNF']['EXS CE SELL'],"CE")
    print("sym",sym,"token",token)
    pushorder(int(df1["FNF"]["Exs Lots"][i]),int(df1["FNF"]["Exs Slice"][i]),sym,token,"BUY",i)
if(int(df1["FNF"]["Force Sell"][1])==1):
    sym,token=gettokenid("FINNIFTY",df1['FNF']['EXS EXP SELL'],df1['FNF']['EXS PE SELL'],"PE")
    print("sym",sym,"token",token)
    pushorder(int(df1["FNF"]["Exs Lots"][i]),int(df1["FNF"]["Exs Slice"][i]),sym,token,"BUY",i)
if(int(df1["FNF"]["Force Sell"][2])==1):
    sym,token=gettokenid("FINNIFTY",df1['FNF']['NEW EXP SELL'],df1['FNF']['NEW CE SELL'],"CE")
    print("sym",sym,"token",token)
    pushorder(int(df1["FNF"]["Lots"][i]),int(df1["FNF"]["Slice"][i]),sym,token,"SELL",i)
if(int(df1["FNF"]["Force Sell"][3])==1):
    sym,token=gettokenid("FINNIFTY",df1['FNF']['NEW EXP SELL'],df1['FNF']['NEW PE SELL'],"PE")
    print("sym",sym,"token",token)
    pushorder(int(df1["FNF"]["Lots"][i]),int(df1["FNF"]["Slice"][i]),sym,token,"SELL",i)

if(int(df1["FNF"]["Force Buy"][0])==1):
    sym,token=gettokenid("FINNIFTY",df1['FNF']['EXS EXP BUY'],df1['FNF']['EXS CE BUY'],"CE")
    print("sym",sym,"token",token)
    pushorder(int(df1["FNF"]["Exs Lots"][i]),int(df1["FNF"]["Exs Slice"][i]),sym,token,"SELL",i)
if(int(df1["FNF"]["Force Buy"][1])==1):
    sym,token=gettokenid("FINNIFTY",df1['FNF']['EXS EXP BUY'],df1['FNF']['EXS PE BUY'],"PE")
    print("sym",sym,"token",token)
    pushorder(int(df1["FNF"]["Exs Lots"][i]),int(df1["FNF"]["Exs Slice"][i]),sym,token,"SELL",i)
if(int(df1["FNF"]["Force Buy"][2])==1):
    sym,token=gettokenid("FINNIFTY",df1['FNF']['NEW EXP BUY'],df1['FNF']['NEW CE BUY'],"CE")
    print("sym",sym,"token",token)
    pushorder(int(df1["FNF"]["Lots"][i]),int(df1["FNF"]["Slice"][i]),sym,token,"BUY",i)
if(int(df1["FNF"]["Force Buy"][3])==1):
    sym,token=gettokenid("FINNIFTY",df1['FNF']['NEW EXP BUY'],df1['FNF']['NEW PE BUY'],"PE")
    pushorder(int(df1["FNF"]["Lots"][i]),int(df1["FNF"]["Slice"][i]),sym,token,"BUY",i)
    print("sym",sym,"token",token)