import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()

    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)

    kk_rct = kk_img.get_rect()
    kk_rct.center=300,200

    tmr = 0

    enn = pg.Surface((20,20))
    pg.draw.circle(enn,(255,0,0),(10,10),10)


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()

        x=-1
        y=0

        if key_lst[pg.K_UP]:
            y-=1
        
        if key_lst[pg.K_DOWN]:
            y+=1

        if key_lst[pg.K_LEFT]:
            x-=1

        if key_lst[pg.K_RIGHT]:
            x+=2

        kk_rct.move_ip((x,y))


        s = tmr%3200

        screen.blit(bg_img, [-s, 0])
        screen.blit(bg_img2,[-s+1600, 0])
        screen.blit(bg_img,[-s+3200, 0])
        screen.blit(bg_img2,[-s+4800, 0])

        screen.blit(kk_img,kk_rct)

        pg.display.update()
        tmr += 1        
        clock.tick(200)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()