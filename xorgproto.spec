#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v5
# autospec commit: c02b2fe
#
# Source0 file verified with key 0x14706DBE1E4B4540 (fourdan@xfce.org)
#
Name     : xorgproto
Version  : 2024.1
Release  : 21
URL      : https://www.x.org/archive/individual/proto/xorgproto-2024.1.tar.gz
Source0  : https://www.x.org/archive/individual/proto/xorgproto-2024.1.tar.gz
Source1  : https://www.x.org/archive/individual/proto/xorgproto-2024.1.tar.gz.sig
Summary  : AppleWM extension headers
Group    : Development/Tools
License  : BSD-2-Clause HPND ICU MIT MIT-Opengroup MIT-feh SGI-B-2.0 X11
Requires: xorgproto-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libxslt-bin
BuildRequires : pkg-config
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xt)
BuildRequires : xmlto
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory contains the specifications of address types for the
ServerInterpreted address family used in the ChangeHost and ListHosts
requests in the X11 Protocol.  See Chapter 9 of the X11 Protocol spec
for more information.

%package dev
Summary: dev components for the xorgproto package.
Group: Development
Provides: xorgproto-devel = %{version}-%{release}
Requires: xorgproto = %{version}-%{release}

%description dev
dev components for the xorgproto package.


%package dev32
Summary: dev32 components for the xorgproto package.
Group: Default
Requires: xorgproto-dev = %{version}-%{release}

%description dev32
dev32 components for the xorgproto package.


%package doc
Summary: doc components for the xorgproto package.
Group: Documentation

%description doc
doc components for the xorgproto package.


%package license
Summary: license components for the xorgproto package.
Group: Default

%description license
license components for the xorgproto package.


%prep
%setup -q -n xorgproto-2024.1
cd %{_builddir}/xorgproto-2024.1
pushd ..
cp -a xorgproto-2024.1 build32
popd
pushd ..
cp -a xorgproto-2024.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711511520
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1711511520
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xorgproto
cp %{_builddir}/xorgproto-%{version}/COPYING-applewmproto %{buildroot}/usr/share/package-licenses/xorgproto/42340fde32d40bfd8d338379870b9980ebcde846 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-bigreqsproto %{buildroot}/usr/share/package-licenses/xorgproto/893c940eb56cd6a45620c65c72b9a8c48bd79217 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-compositeproto %{buildroot}/usr/share/package-licenses/xorgproto/5663d7281a11423245c6029a9b91cebf3870f5d5 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-damageproto %{buildroot}/usr/share/package-licenses/xorgproto/d271044d7dd048bfac0e5ab7aea3666687c9aa2f || :
cp %{_builddir}/xorgproto-%{version}/COPYING-dmxproto %{buildroot}/usr/share/package-licenses/xorgproto/6c394114eefb35de30b9675a99cc1500c6e574cb || :
cp %{_builddir}/xorgproto-%{version}/COPYING-dri2proto %{buildroot}/usr/share/package-licenses/xorgproto/254aec9ad4aa42eb4f11c7a58ea1d297e14c43ae || :
cp %{_builddir}/xorgproto-%{version}/COPYING-dri3proto %{buildroot}/usr/share/package-licenses/xorgproto/124a6c588b14eda9e67225c78979d80b04085eb5 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-evieproto %{buildroot}/usr/share/package-licenses/xorgproto/75d6a96dcba57db8eedae5d71472bcb264c93610 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-fixesproto %{buildroot}/usr/share/package-licenses/xorgproto/df1bc686426d59f220e8c16b7345927f1648e773 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-fontcacheproto %{buildroot}/usr/share/package-licenses/xorgproto/47ca90dc423091f8db250f2cc45f28aba88d11ed || :
cp %{_builddir}/xorgproto-%{version}/COPYING-fontsproto %{buildroot}/usr/share/package-licenses/xorgproto/3c33e98325d414f0290c82bc32b0d8c28cbeeb9b || :
cp %{_builddir}/xorgproto-%{version}/COPYING-glproto %{buildroot}/usr/share/package-licenses/xorgproto/a9fbc5ee6bc3b991c1fee735b96204001a8d64fe || :
cp %{_builddir}/xorgproto-%{version}/COPYING-inputproto %{buildroot}/usr/share/package-licenses/xorgproto/d8b8b6fadbff8363d66d5c703971ab0c86696e26 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-kbproto %{buildroot}/usr/share/package-licenses/xorgproto/cbfdfb0078ac466712aa0a82242b8fc955b0bc00 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-lg3dproto %{buildroot}/usr/share/package-licenses/xorgproto/8258eff701c6fc7c254291f816ba170cc752afdb || :
cp %{_builddir}/xorgproto-%{version}/COPYING-pmproto %{buildroot}/usr/share/package-licenses/xorgproto/0fd34aff7c778553a46ad8bf5d325f493a65a6ac || :
cp %{_builddir}/xorgproto-%{version}/COPYING-presentproto %{buildroot}/usr/share/package-licenses/xorgproto/124a6c588b14eda9e67225c78979d80b04085eb5 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-printproto %{buildroot}/usr/share/package-licenses/xorgproto/8fd381ac9f0abb0c29622229dcfca1e9b30b4099 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-randrproto %{buildroot}/usr/share/package-licenses/xorgproto/5c96c2383498d529b9f62385b9db5ed6f290a890 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-recordproto %{buildroot}/usr/share/package-licenses/xorgproto/618c9d05efe2932bc3aa4745ecfb548303dd8f08 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-renderproto %{buildroot}/usr/share/package-licenses/xorgproto/4882eb6580148a083a7745785ef76768de52086c || :
cp %{_builddir}/xorgproto-%{version}/COPYING-resourceproto %{buildroot}/usr/share/package-licenses/xorgproto/6596e03f9467e3d698993a49289a502c4baf7e08 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-scrnsaverproto %{buildroot}/usr/share/package-licenses/xorgproto/87d59feee73204c7334b7e00ae1cec3f3c583474 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-trapproto %{buildroot}/usr/share/package-licenses/xorgproto/d89dea43c64cc3e1509ca935c2745cb9119d2ad9 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-videoproto %{buildroot}/usr/share/package-licenses/xorgproto/95828c7cb78866a118ce19012faefcd9da321946 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-windowswmproto %{buildroot}/usr/share/package-licenses/xorgproto/9d9197d2f5bab005c1592b820ceed2550f97db19 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-x11proto %{buildroot}/usr/share/package-licenses/xorgproto/c38585ec882f4ccfb985ed8eda6b39737e4b3f36 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-xcmiscproto %{buildroot}/usr/share/package-licenses/xorgproto/bb306f5409529d1c19b78d60f705d37e3c470124 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-xextproto %{buildroot}/usr/share/package-licenses/xorgproto/caf1c560f7638108b748b90a8798b5c4ee54b464 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-xf86bigfontproto %{buildroot}/usr/share/package-licenses/xorgproto/9384394a530b4a93530da89f95e05ac86c4880a0 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-xf86dgaproto %{buildroot}/usr/share/package-licenses/xorgproto/9384394a530b4a93530da89f95e05ac86c4880a0 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-xf86driproto %{buildroot}/usr/share/package-licenses/xorgproto/88aacfcae9d42c894660950b01e7229cc2895cad || :
cp %{_builddir}/xorgproto-%{version}/COPYING-xf86miscproto %{buildroot}/usr/share/package-licenses/xorgproto/9384394a530b4a93530da89f95e05ac86c4880a0 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-xf86rushproto %{buildroot}/usr/share/package-licenses/xorgproto/9384394a530b4a93530da89f95e05ac86c4880a0 || :
cp %{_builddir}/xorgproto-%{version}/COPYING-xf86vidmodeproto %{buildroot}/usr/share/package-licenses/xorgproto/d13c7d638806dc37e5c9b6bbc39366cd904d04de || :
cp %{_builddir}/xorgproto-%{version}/COPYING-xineramaproto %{buildroot}/usr/share/package-licenses/xorgproto/2aa8684f0abf57011bd8bf5c30b0390cc2c85a03 || :
export GOAMD64=v2
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/include/X11/extensions/vldXvMC.h
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/include/X11/extensions/xf86vm.h
/usr/include/X11/extensions/xf86vmproto.h
/usr/include/X11/extensions/xf86vmstr.h
/usr/include/X11/extensions/xfixesproto.h
/usr/include/X11/extensions/xfixeswire.h
/usr/include/X11/extensions/xtestconst.h
/usr/include/X11/extensions/xtestext1const.h
/usr/include/X11/extensions/xtestext1proto.h
/usr/include/X11/extensions/xtestproto.h
/usr/include/X11/extensions/xwaylandproto.h
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
/usr/lib64/pkgconfig/dpmsproto.pc
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
/usr/lib64/pkgconfig/videoproto.pc
/usr/lib64/pkgconfig/xcmiscproto.pc
/usr/lib64/pkgconfig/xextproto.pc
/usr/lib64/pkgconfig/xf86bigfontproto.pc
/usr/lib64/pkgconfig/xf86dgaproto.pc
/usr/lib64/pkgconfig/xf86driproto.pc
/usr/lib64/pkgconfig/xf86vidmodeproto.pc
/usr/lib64/pkgconfig/xineramaproto.pc
/usr/lib64/pkgconfig/xproto.pc
/usr/lib64/pkgconfig/xwaylandproto.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/pkgconfig/32applewmproto.pc
/usr/lib32/pkgconfig/32bigreqsproto.pc
/usr/lib32/pkgconfig/32compositeproto.pc
/usr/lib32/pkgconfig/32damageproto.pc
/usr/lib32/pkgconfig/32dmxproto.pc
/usr/lib32/pkgconfig/32dpmsproto.pc
/usr/lib32/pkgconfig/32dri2proto.pc
/usr/lib32/pkgconfig/32dri3proto.pc
/usr/lib32/pkgconfig/32fixesproto.pc
/usr/lib32/pkgconfig/32fontsproto.pc
/usr/lib32/pkgconfig/32glproto.pc
/usr/lib32/pkgconfig/32inputproto.pc
/usr/lib32/pkgconfig/32kbproto.pc
/usr/lib32/pkgconfig/32presentproto.pc
/usr/lib32/pkgconfig/32randrproto.pc
/usr/lib32/pkgconfig/32recordproto.pc
/usr/lib32/pkgconfig/32renderproto.pc
/usr/lib32/pkgconfig/32resourceproto.pc
/usr/lib32/pkgconfig/32scrnsaverproto.pc
/usr/lib32/pkgconfig/32videoproto.pc
/usr/lib32/pkgconfig/32xcmiscproto.pc
/usr/lib32/pkgconfig/32xextproto.pc
/usr/lib32/pkgconfig/32xf86bigfontproto.pc
/usr/lib32/pkgconfig/32xf86dgaproto.pc
/usr/lib32/pkgconfig/32xf86driproto.pc
/usr/lib32/pkgconfig/32xf86vidmodeproto.pc
/usr/lib32/pkgconfig/32xineramaproto.pc
/usr/lib32/pkgconfig/32xproto.pc
/usr/lib32/pkgconfig/32xwaylandproto.pc
/usr/lib32/pkgconfig/applewmproto.pc
/usr/lib32/pkgconfig/bigreqsproto.pc
/usr/lib32/pkgconfig/compositeproto.pc
/usr/lib32/pkgconfig/damageproto.pc
/usr/lib32/pkgconfig/dmxproto.pc
/usr/lib32/pkgconfig/dpmsproto.pc
/usr/lib32/pkgconfig/dri2proto.pc
/usr/lib32/pkgconfig/dri3proto.pc
/usr/lib32/pkgconfig/fixesproto.pc
/usr/lib32/pkgconfig/fontsproto.pc
/usr/lib32/pkgconfig/glproto.pc
/usr/lib32/pkgconfig/inputproto.pc
/usr/lib32/pkgconfig/kbproto.pc
/usr/lib32/pkgconfig/presentproto.pc
/usr/lib32/pkgconfig/randrproto.pc
/usr/lib32/pkgconfig/recordproto.pc
/usr/lib32/pkgconfig/renderproto.pc
/usr/lib32/pkgconfig/resourceproto.pc
/usr/lib32/pkgconfig/scrnsaverproto.pc
/usr/lib32/pkgconfig/videoproto.pc
/usr/lib32/pkgconfig/xcmiscproto.pc
/usr/lib32/pkgconfig/xextproto.pc
/usr/lib32/pkgconfig/xf86bigfontproto.pc
/usr/lib32/pkgconfig/xf86dgaproto.pc
/usr/lib32/pkgconfig/xf86driproto.pc
/usr/lib32/pkgconfig/xf86vidmodeproto.pc
/usr/lib32/pkgconfig/xineramaproto.pc
/usr/lib32/pkgconfig/xproto.pc
/usr/lib32/pkgconfig/xwaylandproto.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/bigreqsproto/bigreq.xml
/usr/share/doc/fontsproto/fsproto.xml
/usr/share/doc/kbproto/XKBproto-1.svg
/usr/share/doc/kbproto/XKBproto-10.svg
/usr/share/doc/kbproto/XKBproto-11.svg
/usr/share/doc/kbproto/XKBproto-2.svg
/usr/share/doc/kbproto/XKBproto-3.svg
/usr/share/doc/kbproto/XKBproto-4.svg
/usr/share/doc/kbproto/XKBproto-5.svg
/usr/share/doc/kbproto/XKBproto-6.svg
/usr/share/doc/kbproto/XKBproto-7.svg
/usr/share/doc/kbproto/XKBproto-8.svg
/usr/share/doc/kbproto/XKBproto-9.svg
/usr/share/doc/kbproto/acknowledgements.xml
/usr/share/doc/kbproto/appA.xml
/usr/share/doc/kbproto/appB.xml
/usr/share/doc/kbproto/appC.xml
/usr/share/doc/kbproto/appD.xml
/usr/share/doc/kbproto/ch01.xml
/usr/share/doc/kbproto/ch02.xml
/usr/share/doc/kbproto/ch03.xml
/usr/share/doc/kbproto/ch04.xml
/usr/share/doc/kbproto/ch05.xml
/usr/share/doc/kbproto/ch06.xml
/usr/share/doc/kbproto/ch07.xml
/usr/share/doc/kbproto/ch08.xml
/usr/share/doc/kbproto/ch09.xml
/usr/share/doc/kbproto/ch10.xml
/usr/share/doc/kbproto/ch11.xml
/usr/share/doc/kbproto/ch12.xml
/usr/share/doc/kbproto/ch13.xml
/usr/share/doc/kbproto/ch14.xml
/usr/share/doc/kbproto/ch15.xml
/usr/share/doc/kbproto/ch16.xml
/usr/share/doc/kbproto/xkbproto.xml
/usr/share/doc/recordproto/record.xml
/usr/share/doc/scrnsaverproto/saver.xml
/usr/share/doc/xcmiscproto/xc-misc.xml
/usr/share/doc/xextproto/appendix.xml
/usr/share/doc/xextproto/appgrp.xml
/usr/share/doc/xextproto/dbe.xml
/usr/share/doc/xextproto/dpms.xml
/usr/share/doc/xextproto/evi.xml
/usr/share/doc/xextproto/geproto.xml
/usr/share/doc/xextproto/lbx.xml
/usr/share/doc/xextproto/multibuf.xml
/usr/share/doc/xextproto/security.xml
/usr/share/doc/xextproto/shape.xml
/usr/share/doc/xextproto/shm.xml
/usr/share/doc/xextproto/sync.xml
/usr/share/doc/xextproto/tog-cup.xml
/usr/share/doc/xextproto/xtest.xml
/usr/share/doc/xorgproto/*
/usr/share/doc/xproto/encoding.xml
/usr/share/doc/xproto/glossary.xml
/usr/share/doc/xproto/keysyms.xml
/usr/share/doc/xproto/sect1-9.xml
/usr/share/doc/xproto/x11protocol.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xorgproto/0fd34aff7c778553a46ad8bf5d325f493a65a6ac
/usr/share/package-licenses/xorgproto/124a6c588b14eda9e67225c78979d80b04085eb5
/usr/share/package-licenses/xorgproto/254aec9ad4aa42eb4f11c7a58ea1d297e14c43ae
/usr/share/package-licenses/xorgproto/2aa8684f0abf57011bd8bf5c30b0390cc2c85a03
/usr/share/package-licenses/xorgproto/3c33e98325d414f0290c82bc32b0d8c28cbeeb9b
/usr/share/package-licenses/xorgproto/42340fde32d40bfd8d338379870b9980ebcde846
/usr/share/package-licenses/xorgproto/47ca90dc423091f8db250f2cc45f28aba88d11ed
/usr/share/package-licenses/xorgproto/4882eb6580148a083a7745785ef76768de52086c
/usr/share/package-licenses/xorgproto/5663d7281a11423245c6029a9b91cebf3870f5d5
/usr/share/package-licenses/xorgproto/5c96c2383498d529b9f62385b9db5ed6f290a890
/usr/share/package-licenses/xorgproto/618c9d05efe2932bc3aa4745ecfb548303dd8f08
/usr/share/package-licenses/xorgproto/6596e03f9467e3d698993a49289a502c4baf7e08
/usr/share/package-licenses/xorgproto/6c394114eefb35de30b9675a99cc1500c6e574cb
/usr/share/package-licenses/xorgproto/75d6a96dcba57db8eedae5d71472bcb264c93610
/usr/share/package-licenses/xorgproto/8258eff701c6fc7c254291f816ba170cc752afdb
/usr/share/package-licenses/xorgproto/87d59feee73204c7334b7e00ae1cec3f3c583474
/usr/share/package-licenses/xorgproto/88aacfcae9d42c894660950b01e7229cc2895cad
/usr/share/package-licenses/xorgproto/893c940eb56cd6a45620c65c72b9a8c48bd79217
/usr/share/package-licenses/xorgproto/8fd381ac9f0abb0c29622229dcfca1e9b30b4099
/usr/share/package-licenses/xorgproto/9384394a530b4a93530da89f95e05ac86c4880a0
/usr/share/package-licenses/xorgproto/95828c7cb78866a118ce19012faefcd9da321946
/usr/share/package-licenses/xorgproto/9d9197d2f5bab005c1592b820ceed2550f97db19
/usr/share/package-licenses/xorgproto/a9fbc5ee6bc3b991c1fee735b96204001a8d64fe
/usr/share/package-licenses/xorgproto/bb306f5409529d1c19b78d60f705d37e3c470124
/usr/share/package-licenses/xorgproto/c38585ec882f4ccfb985ed8eda6b39737e4b3f36
/usr/share/package-licenses/xorgproto/caf1c560f7638108b748b90a8798b5c4ee54b464
/usr/share/package-licenses/xorgproto/cbfdfb0078ac466712aa0a82242b8fc955b0bc00
/usr/share/package-licenses/xorgproto/d13c7d638806dc37e5c9b6bbc39366cd904d04de
/usr/share/package-licenses/xorgproto/d271044d7dd048bfac0e5ab7aea3666687c9aa2f
/usr/share/package-licenses/xorgproto/d89dea43c64cc3e1509ca935c2745cb9119d2ad9
/usr/share/package-licenses/xorgproto/d8b8b6fadbff8363d66d5c703971ab0c86696e26
/usr/share/package-licenses/xorgproto/df1bc686426d59f220e8c16b7345927f1648e773
