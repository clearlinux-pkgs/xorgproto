#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5B8A2D50A0ECD0D3 (ajax@nwnk.net)
#
Name     : xorgproto
Version  : 2018.4
Release  : 2
URL      : https://www.x.org/archive/individual/proto/xorgproto-2018.4.tar.gz
Source0  : https://www.x.org/archive/individual/proto/xorgproto-2018.4.tar.gz
Source99 : https://www.x.org/archive/individual/proto/xorgproto-2018.4.tar.gz.sig
Summary  : Render extension headers
Group    : Development/Tools
License  : 2BSD HPND ICU MIT MIT-Opengroup MIT-feh SGI-B-2.0 X11
Requires: xorgproto-doc
BuildRequires : libxslt-bin
BuildRequires : meson
BuildRequires : ninja
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : python3
BuildRequires : xmlto

%description
X Window System Unified Protocol
This package provides the headers and specification documents defining
the core protocol and (many) extensions for the X Window System. The
extensions are those common among servers descended from X.Org 6.7. It
also includes a number of headers that aren't purely protocol related,
but are depended upon by many other X Window System packages to provide
common definitions and porting layer.

%package dev
Summary: dev components for the xorgproto package.
Group: Development
Provides: xorgproto-devel

%description dev
dev components for the xorgproto package.


%package doc
Summary: doc components for the xorgproto package.
Group: Documentation

%description doc
doc components for the xorgproto package.


%prep
%setup -q -n xorgproto-2018.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526133250
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1526133250
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/GL/glxint.h
/usr/include/GL/glxmd.h
/usr/include/GL/glxproto.h
/usr/include/GL/glxtokens.h
/usr/include/GL/internal/glcore.h
/usr/include/X11/DECkeysym.h
/usr/include/X11/HPkeysym.h
/usr/include/X11/PM/PM.h
/usr/include/X11/PM/PMproto.h
/usr/include/X11/Sunkeysym.h
/usr/include/X11/X.h
/usr/include/X11/XF86keysym.h
/usr/include/X11/XWDFile.h
/usr/include/X11/Xalloca.h
/usr/include/X11/Xarch.h
/usr/include/X11/Xatom.h
/usr/include/X11/Xdefs.h
/usr/include/X11/Xfuncproto.h
/usr/include/X11/Xfuncs.h
/usr/include/X11/Xmd.h
/usr/include/X11/Xos.h
/usr/include/X11/Xos_r.h
/usr/include/X11/Xosdefs.h
/usr/include/X11/Xpoll.h
/usr/include/X11/Xproto.h
/usr/include/X11/Xprotostr.h
/usr/include/X11/Xthreads.h
/usr/include/X11/Xw32defs.h
/usr/include/X11/Xwindows.h
/usr/include/X11/Xwinsock.h
/usr/include/X11/ap_keysym.h
/usr/include/X11/dri/xf86dri.h
/usr/include/X11/dri/xf86driproto.h
/usr/include/X11/dri/xf86dristr.h
/usr/include/X11/extensions/EVI.h
/usr/include/X11/extensions/EVIproto.h
/usr/include/X11/extensions/XI.h
/usr/include/X11/extensions/XI2.h
/usr/include/X11/extensions/XI2proto.h
/usr/include/X11/extensions/XIproto.h
/usr/include/X11/extensions/XKB.h
/usr/include/X11/extensions/XKBgeom.h
/usr/include/X11/extensions/XKBproto.h
/usr/include/X11/extensions/XKBsrv.h
/usr/include/X11/extensions/XKBstr.h
/usr/include/X11/extensions/XResproto.h
/usr/include/X11/extensions/Xv.h
/usr/include/X11/extensions/XvMC.h
/usr/include/X11/extensions/XvMCproto.h
/usr/include/X11/extensions/Xvproto.h
/usr/include/X11/extensions/ag.h
/usr/include/X11/extensions/agproto.h
/usr/include/X11/extensions/applewmconst.h
/usr/include/X11/extensions/applewmproto.h
/usr/include/X11/extensions/bigreqsproto.h
/usr/include/X11/extensions/bigreqstr.h
/usr/include/X11/extensions/composite.h
/usr/include/X11/extensions/compositeproto.h
/usr/include/X11/extensions/cup.h
/usr/include/X11/extensions/cupproto.h
/usr/include/X11/extensions/damageproto.h
/usr/include/X11/extensions/damagewire.h
/usr/include/X11/extensions/dbe.h
/usr/include/X11/extensions/dbeproto.h
/usr/include/X11/extensions/dmx.h
/usr/include/X11/extensions/dmxproto.h
/usr/include/X11/extensions/dpmsconst.h
/usr/include/X11/extensions/dpmsproto.h
/usr/include/X11/extensions/dri2proto.h
/usr/include/X11/extensions/dri2tokens.h
/usr/include/X11/extensions/dri3proto.h
/usr/include/X11/extensions/ge.h
/usr/include/X11/extensions/geproto.h
/usr/include/X11/extensions/lbx.h
/usr/include/X11/extensions/lbxproto.h
/usr/include/X11/extensions/mitmiscconst.h
/usr/include/X11/extensions/mitmiscproto.h
/usr/include/X11/extensions/multibufconst.h
/usr/include/X11/extensions/multibufproto.h
/usr/include/X11/extensions/panoramiXproto.h
/usr/include/X11/extensions/presentproto.h
/usr/include/X11/extensions/presenttokens.h
/usr/include/X11/extensions/randr.h
/usr/include/X11/extensions/randrproto.h
/usr/include/X11/extensions/recordconst.h
/usr/include/X11/extensions/recordproto.h
/usr/include/X11/extensions/recordstr.h
/usr/include/X11/extensions/render.h
/usr/include/X11/extensions/renderproto.h
/usr/include/X11/extensions/saver.h
/usr/include/X11/extensions/saverproto.h
/usr/include/X11/extensions/secur.h
/usr/include/X11/extensions/securproto.h
/usr/include/X11/extensions/shapeconst.h
/usr/include/X11/extensions/shapeproto.h
/usr/include/X11/extensions/shapestr.h
/usr/include/X11/extensions/shm.h
/usr/include/X11/extensions/shmproto.h
/usr/include/X11/extensions/shmstr.h
/usr/include/X11/extensions/syncconst.h
/usr/include/X11/extensions/syncproto.h
/usr/include/X11/extensions/syncstr.h
/usr/include/X11/extensions/vldXvMC.h
/usr/include/X11/extensions/windowswm.h
/usr/include/X11/extensions/windowswmstr.h
/usr/include/X11/extensions/xcmiscproto.h
/usr/include/X11/extensions/xcmiscstr.h
/usr/include/X11/extensions/xf86bigfont.h
/usr/include/X11/extensions/xf86bigfproto.h
/usr/include/X11/extensions/xf86bigfstr.h
/usr/include/X11/extensions/xf86dga.h
/usr/include/X11/extensions/xf86dga1const.h
/usr/include/X11/extensions/xf86dga1proto.h
/usr/include/X11/extensions/xf86dga1str.h
/usr/include/X11/extensions/xf86dgaconst.h
/usr/include/X11/extensions/xf86dgaproto.h
/usr/include/X11/extensions/xf86dgastr.h
/usr/include/X11/extensions/xf86misc.h
/usr/include/X11/extensions/xf86mscstr.h
/usr/include/X11/extensions/xf86vm.h
/usr/include/X11/extensions/xf86vmproto.h
/usr/include/X11/extensions/xf86vmstr.h
/usr/include/X11/extensions/xfixesproto.h
/usr/include/X11/extensions/xfixeswire.h
/usr/include/X11/extensions/xtestconst.h
/usr/include/X11/extensions/xtestext1const.h
/usr/include/X11/extensions/xtestext1proto.h
/usr/include/X11/extensions/xtestproto.h
/usr/include/X11/extensions/xtrapbits.h
/usr/include/X11/extensions/xtrapddmi.h
/usr/include/X11/extensions/xtrapdi.h
/usr/include/X11/extensions/xtrapemacros.h
/usr/include/X11/extensions/xtraplib.h
/usr/include/X11/extensions/xtraplibp.h
/usr/include/X11/extensions/xtrapproto.h
/usr/include/X11/fonts/FS.h
/usr/include/X11/fonts/FSproto.h
/usr/include/X11/fonts/font.h
/usr/include/X11/fonts/fontproto.h
/usr/include/X11/fonts/fontstruct.h
/usr/include/X11/fonts/fsmasks.h
/usr/include/X11/keysym.h
/usr/include/X11/keysymdef.h
/usr/lib64/pkgconfig/applewmproto.pc
/usr/lib64/pkgconfig/bigreqsproto.pc
/usr/lib64/pkgconfig/compositeproto.pc
/usr/lib64/pkgconfig/damageproto.pc
/usr/lib64/pkgconfig/dmxproto.pc
/usr/lib64/pkgconfig/dri2proto.pc
/usr/lib64/pkgconfig/dri3proto.pc
/usr/lib64/pkgconfig/fixesproto.pc
/usr/lib64/pkgconfig/fontsproto.pc
/usr/lib64/pkgconfig/glproto.pc
/usr/lib64/pkgconfig/inputproto.pc
/usr/lib64/pkgconfig/kbproto.pc
/usr/lib64/pkgconfig/presentproto.pc
/usr/lib64/pkgconfig/randrproto.pc
/usr/lib64/pkgconfig/recordproto.pc
/usr/lib64/pkgconfig/renderproto.pc
/usr/lib64/pkgconfig/resourceproto.pc
/usr/lib64/pkgconfig/scrnsaverproto.pc
/usr/lib64/pkgconfig/trapproto.pc
/usr/lib64/pkgconfig/videoproto.pc
/usr/lib64/pkgconfig/windowswmproto.pc
/usr/lib64/pkgconfig/xcmiscproto.pc
/usr/lib64/pkgconfig/xextproto.pc
/usr/lib64/pkgconfig/xf86bigfontproto.pc
/usr/lib64/pkgconfig/xf86dgaproto.pc
/usr/lib64/pkgconfig/xf86driproto.pc
/usr/lib64/pkgconfig/xf86miscproto.pc
/usr/lib64/pkgconfig/xf86vidmodeproto.pc
/usr/lib64/pkgconfig/xineramaproto.pc
/usr/lib64/pkgconfig/xproto.pc
/usr/lib64/pkgconfig/xproxymngproto.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/xorgproto/*
