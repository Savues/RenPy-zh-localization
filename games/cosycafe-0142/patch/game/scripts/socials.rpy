screen socials():

    tag menu

    use game_menu('socials', scroll='frame'):

        frame background None:
            xycenter (.5 , .5 )
            align    (.5 , .5 )
            xysize   (443, 633)
            frame background None:
                xycenter (.5 , .5 )
                align    (.5 , .5 )
                xysize   (411, 601)
                vbox:
                    yfill True
                    spacing 8
                    xycenter (.5 , .5 )
                    xysize   (411, 601)
                    offset   (0  , 1  )
                    frame background None: # Cosy Cafe
                        xysize (411, 45)
                        xycenter (.5, .5)
                        text 'Cosy Cafe' align (.5, .5) offset (0, 0) font "fonts/MiSans-Regular.ttf" size 45

                    frame background None: # Bio
                        xysize (411, 175)
                        xycenter (.5, .5)
                        text _p("欢迎在 Patreon 或 SubStar 上支持 Cosy Cafe：可提前一个月体验新内容，还能频繁看到关于游戏进度的开发日志。当然，也欢迎来 Discord 上聊聊天，我们随时恭候！") align (.5, .5) text_align .5 font "fonts/MiSans-Regular.ttf" size 22
                    frame background None: # Socials
                        xysize   (411, 357)
                        xycenter (.5, .5 )
                        vbox:
                            xycenter (.5, .5)
                            align    (.5, .0)
                            offset   ( 0, -6)
                            spacing 8
                            frame background None:
                                xysize (411, 83)
                                xycenter (.5, .5)
                                button:

                                    action OpenURL('https://www.patreon.com/cosycreator')
                                    
                                    frame background None:
                                        xysize (411, 83)
                                        xycenter (.5, .5)
                                        image AlphaMask(At("gui/msp1/socials/patreon bg.png", socials()), "gui/msp1/socials/socials_button.png") offset (-6, -6)
                                        frame background None:
                                            align    (.5 , .5  )
                                            xycenter (.5 , .5  )
                                            xysize   (364, None)
                                            image "gui/msp1/socials/patreon.png" xycenter (.5, .5) align (.0, .5)
                                            text "patreon".upper() xycenter (.5, .5) align (1.0, .5) text_align 1.0 offset (0, -2) font "fonts/MiSans-Regular.ttf" size 33
                                    xycenter (.5 , .5  )
                                    at button_cascade_bottom(.0)
                            frame background None:
                                xysize (411, 83)
                                xycenter (.5, .5)
                                button:

                                    action OpenURL('https://subscribestar.adult/cosy-creator')
                                    
                                    frame background None:
                                        xysize (411, 83)
                                        xycenter (.5, .5)
                                        image AlphaMask(At("gui/msp1/socials/ss bg.png", socials()), "gui/msp1/socials/socials_button.png") offset (-6, -6)
                                        frame background None:
                                            align    (.5 , .5  )
                                            xycenter (.5 , .5  )
                                            xysize   (364, None)
                                            image "gui/msp1/socials/ss.png" xycenter (.5, .5) align (.0, .5)
                                            text "subscribestar".upper() xycenter (.5, .5) align (1.0, .5) text_align 1.0 offset (0, -2) font "fonts/MiSans-Regular.ttf" size 33
                                    xycenter (.5 , .5  )
                                    at button_cascade_bottom(.05)
                            frame background None:
                                xysize (411, 83)
                                xycenter (.5, .5)
                                button:

                                    action OpenURL('https://discord.gg/U9CwvDf2vV')
                                    
                                    frame background None:
                                        xysize (411, 83)
                                        xycenter (.5, .5)
                                        image AlphaMask(At("gui/msp1/socials/discord bg.png", socials()), "gui/msp1/socials/socials_button.png") offset (-6, -6)
                                        frame background None:
                                            align    (.5 , .5  )
                                            xycenter (.5 , .5  )
                                            xysize   (364, None)
                                            image "gui/msp1/socials/discord.png" xycenter (.5, .5) align (.0, .5)
                                            text "discord".upper() xycenter (.5, .5) align (1.0, .5) text_align 1.0 offset (0, -2) font "fonts/MiSans-Regular.ttf" size 33
                                    xycenter (.5 , .5  )
                                    at button_cascade_bottom(.1)
                            frame background None:
                                xysize (411, 83)
                                xycenter (.5, .5)
                                button:

                                    action OpenURL('https://cosy-creator.itch.io/cosy-cafe')
                                    
                                    frame background None:
                                        xysize (411, 83)
                                        xycenter (.5, .5)
                                        image AlphaMask(At("gui/msp1/socials/itch bg.png", socials()), "gui/msp1/socials/socials_button.png") offset (-6, -6)
                                        frame background None:
                                            align    (.5 , .5  )
                                            xycenter (.5 , .5  )
                                            xysize   (364, None)
                                            image "gui/msp1/socials/itch io.png" xycenter (.5, .5) align (.0, .5)
                                            text "itch.io".upper() xycenter (.5, .5) align (1.0, .5) text_align 1.0 offset (0, -2) font "fonts/MiSans-Regular.ttf" size 33
                                    xycenter (.5, .5)
                                    at button_cascade_bottom(.15)