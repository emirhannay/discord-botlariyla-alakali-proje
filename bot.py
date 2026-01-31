@bot.command()
async def yardım(ctx):
    await ctx.send("Komutlar:\n$hello \n$heh\n$temizle [miktar]\n$gecikme\n$yardım")

@bot.command()
async def randomemojigonderenfonksiyon(ctx):
    #await ctx.send(randomemoji())
    await ctx.send("yukarıdaki kod düzenlenmeli")


@bot.command()
async def gecikme(ctx):
    gecikme_ms = round(bot.latency * 1000)
    await ctx.send(f"Bot gecikmesi: {gecikme_ms}ms ⏱️")
