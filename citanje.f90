program test

    real, parameter :: nbo=50., sbo=41.9, ebo=27., wbo=16.2, dx=0.1, dy=0.1
    integer, parameter :: im=1.5+(ebo-wbo)/dx, jm=1.5+(nbo-sbo)/dy,idxgm=6847
    integer, parameter :: iym=50,imm=12,iyst=1961
    real, dimension (im,jm) :: rr
    integer, dimension (idxgm) :: idxg,idxf,gco,iloc,jloc
    real, dimension (idxgm) :: rr1D,glon,glat
    integer, dimension (imm) ::  mnd
    character*5 lyr,adum
    
    data mnd/31,28,31,30,31,30,31,31,30,31,30,31/
    
    print *, 'im,jm,im*jm',im,jm,im*jm
    
    !====  READ COORDINATE OF POINTS ======================================
        open(12,file='TG/PredtandfilaGrid.dat')
        read(12,*) adum
      do ix=1,idxgm
        read(12,*) idxg(ix),glon(ix),glat(ix),gco(ix)
      enddo
    !======================================================================
    
    ix=idxgm
    !print *, idxg(ix),glon(ix),glat(ix),gco(ix)
    
    open (99,file='out.dat')
    do ix=1,idxgm
    iloc(ix)=1.5+((glon(ix)-wbo)/dx)
    jloc(ix)=1.5+((glat(ix)-sbo)/dy)
    write (99,*) glon(ix),glat(ix),iloc(ix),jloc(ix)
    enddo
    
    open(13,file='grd/TG_carpath.grd',access='direct',recl=im*jm*4)
    open(14,file='grd/TG_carpath.ctl')
    
    open(20,file='TG/CARPATGRID_TA_D.ser')
    read(20,*) (idxf(i),i=1,idxgm)
    
    ir=0
      do iy=1,iym
         iyear = iyst+iy-1
           iry = 0
           lyr = 'NLEAP'
    
            do imo=1,imm
              mnd(2)=28
              if(mod(iyear,4).eq.0.and.iyear.ne.2100) mnd(2)=29
    
                do id=1,mnd(imo)
                  ir  = ir+1
                  iry = iry+1
                    read(20,*) iyf,imf,idf,(rr1D(i),i=1,idxgm)
    
                    rr=-999.00
    
                      do ix=1,idxgm
                        rr(iloc(ix),jloc(ix))=rr1D(ix)
                      enddo
    
                enddo ! dan
           enddo ! mesec
    !        print *, lyr,iyear,ir,iry,iyf,imf,idf
      enddo ! godina
    
    close(20)
    close(13)
    
    write(14,*) 'dset TG_carpath.grd'
    write(14,*) 'title carpath'
    write(14,*) 'undef  -999.00'
    write(14,*) 'xdef ',im,' linear ',wbo,dx
    write(14,*) 'ydef ',jm,' linear  ',sbo,dy
    write(14,*) 'zdef 1 levels 1'
    write(14,*) 'tdef ',ir,' linear 00Z01jan1961 24HR'
    write(14,*) 'vars 1'
    write(14,*) 'TG 0 11,1,0  BAT'
    write(14,*) 'endvars'
    
    stop
    end