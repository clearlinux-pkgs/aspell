#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0xB6D9D0CC38B327D7 (kevin@atkinson.dhs.org)
#
Name     : aspell
Version  : 0.60.8.1
Release  : 32
URL      : https://mirrors.kernel.org/gnu/aspell/aspell-0.60.8.1.tar.gz
Source0  : https://mirrors.kernel.org/gnu/aspell/aspell-0.60.8.1.tar.gz
Source1  : https://mirrors.kernel.org/gnu/aspell/aspell-0.60.8.1.tar.gz.sig
Source2  : B6D9D0CC38B327D7.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.1 LGPL-2.1
Requires: aspell-bin = %{version}-%{release}
Requires: aspell-info = %{version}-%{release}
Requires: aspell-lib = %{version}-%{release}
Requires: aspell-license = %{version}-%{release}
Requires: aspell-locales = %{version}-%{release}
Requires: aspell-man = %{version}-%{release}
Requires: aspell-en
Requires: aspell-pt_BR
BuildRequires : buildreq-configure
BuildRequires : gnupg
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Appendix A Installing
*********************
Aspell requires gcc 2.95 (or better) as the C++ compiler.  Other C++
compilers should work with some effort.  Other C++ compilers for mostly
POSIX compliant (Unix, Linux, BeOS, Cygwin) systems should work without
any major problems provided that the compile can handle all of the
advanced C++ features Aspell uses.  C++ compilers for non-Unix systems
might work but it will take some work.  Aspell at very least requires a
Unix-like environment ('sh', 'grep', 'sed', 'tr', ...), and Perl in
order to build.  Aspell also uses a few POSIX functions when necessary.

%package bin
Summary: bin components for the aspell package.
Group: Binaries
Requires: aspell-license = %{version}-%{release}

%description bin
bin components for the aspell package.


%package dev
Summary: dev components for the aspell package.
Group: Development
Requires: aspell-lib = %{version}-%{release}
Requires: aspell-bin = %{version}-%{release}
Provides: aspell-devel = %{version}-%{release}
Requires: aspell = %{version}-%{release}

%description dev
dev components for the aspell package.


%package info
Summary: info components for the aspell package.
Group: Default

%description info
info components for the aspell package.


%package lib
Summary: lib components for the aspell package.
Group: Libraries
Requires: aspell-license = %{version}-%{release}

%description lib
lib components for the aspell package.


%package license
Summary: license components for the aspell package.
Group: Default

%description license
license components for the aspell package.


%package locales
Summary: locales components for the aspell package.
Group: Default

%description locales
locales components for the aspell package.


%package man
Summary: man components for the aspell package.
Group: Default

%description man
man components for the aspell package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) B6D9D0CC38B327D7' gpg.status
%setup -q -n aspell-0.60.8.1
cd %{_builddir}/aspell-0.60.8.1
pushd ..
cp -a aspell-0.60.8.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713221465
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
export SOURCE_DATE_EPOCH=1713221465
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/aspell
cp %{_builddir}/aspell-%{version}/COPYING %{buildroot}/usr/share/package-licenses/aspell/e60c2e780886f95df9c9ee36992b8edabec00bcc || :
cp %{_builddir}/aspell-%{version}/manual/aspell-dev.html/Copying.html %{buildroot}/usr/share/package-licenses/aspell/bfaf730612ae1e838f897dc93179cf6960e9bb43 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang aspell
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/aspell-0.60/ccpp.amf
/usr/lib64/aspell-0.60/comment.amf
/usr/lib64/aspell-0.60/context-filter.info
/usr/lib64/aspell-0.60/cp1250.cmap
/usr/lib64/aspell-0.60/cp1250.cset
/usr/lib64/aspell-0.60/cp1251.cmap
/usr/lib64/aspell-0.60/cp1251.cset
/usr/lib64/aspell-0.60/cp1252.cmap
/usr/lib64/aspell-0.60/cp1252.cset
/usr/lib64/aspell-0.60/cp1253.cmap
/usr/lib64/aspell-0.60/cp1253.cset
/usr/lib64/aspell-0.60/cp1254.cmap
/usr/lib64/aspell-0.60/cp1254.cset
/usr/lib64/aspell-0.60/cp1255.cmap
/usr/lib64/aspell-0.60/cp1255.cset
/usr/lib64/aspell-0.60/cp1256.cmap
/usr/lib64/aspell-0.60/cp1256.cset
/usr/lib64/aspell-0.60/cp1257.cmap
/usr/lib64/aspell-0.60/cp1257.cset
/usr/lib64/aspell-0.60/cp1258.cmap
/usr/lib64/aspell-0.60/cp1258.cset
/usr/lib64/aspell-0.60/dvorak.kbd
/usr/lib64/aspell-0.60/email-filter.info
/usr/lib64/aspell-0.60/email.amf
/usr/lib64/aspell-0.60/html-filter.info
/usr/lib64/aspell-0.60/html.amf
/usr/lib64/aspell-0.60/iso-8859-1.cmap
/usr/lib64/aspell-0.60/iso-8859-1.cset
/usr/lib64/aspell-0.60/iso-8859-10.cmap
/usr/lib64/aspell-0.60/iso-8859-10.cset
/usr/lib64/aspell-0.60/iso-8859-11.cmap
/usr/lib64/aspell-0.60/iso-8859-11.cset
/usr/lib64/aspell-0.60/iso-8859-13.cmap
/usr/lib64/aspell-0.60/iso-8859-13.cset
/usr/lib64/aspell-0.60/iso-8859-14.cmap
/usr/lib64/aspell-0.60/iso-8859-14.cset
/usr/lib64/aspell-0.60/iso-8859-15.cmap
/usr/lib64/aspell-0.60/iso-8859-15.cset
/usr/lib64/aspell-0.60/iso-8859-16.cmap
/usr/lib64/aspell-0.60/iso-8859-16.cset
/usr/lib64/aspell-0.60/iso-8859-2.cmap
/usr/lib64/aspell-0.60/iso-8859-2.cset
/usr/lib64/aspell-0.60/iso-8859-3.cmap
/usr/lib64/aspell-0.60/iso-8859-3.cset
/usr/lib64/aspell-0.60/iso-8859-4.cmap
/usr/lib64/aspell-0.60/iso-8859-4.cset
/usr/lib64/aspell-0.60/iso-8859-5.cmap
/usr/lib64/aspell-0.60/iso-8859-5.cset
/usr/lib64/aspell-0.60/iso-8859-6.cmap
/usr/lib64/aspell-0.60/iso-8859-6.cset
/usr/lib64/aspell-0.60/iso-8859-7.cmap
/usr/lib64/aspell-0.60/iso-8859-7.cset
/usr/lib64/aspell-0.60/iso-8859-8.cmap
/usr/lib64/aspell-0.60/iso-8859-8.cset
/usr/lib64/aspell-0.60/iso-8859-9.cmap
/usr/lib64/aspell-0.60/iso-8859-9.cset
/usr/lib64/aspell-0.60/ispell
/usr/lib64/aspell-0.60/koi8-r.cmap
/usr/lib64/aspell-0.60/koi8-r.cset
/usr/lib64/aspell-0.60/koi8-u.cmap
/usr/lib64/aspell-0.60/koi8-u.cset
/usr/lib64/aspell-0.60/markdown-filter.info
/usr/lib64/aspell-0.60/markdown.amf
/usr/lib64/aspell-0.60/none.amf
/usr/lib64/aspell-0.60/nroff-filter.info
/usr/lib64/aspell-0.60/nroff.amf
/usr/lib64/aspell-0.60/perl.amf
/usr/lib64/aspell-0.60/sgml-filter.info
/usr/lib64/aspell-0.60/sgml.amf
/usr/lib64/aspell-0.60/spell
/usr/lib64/aspell-0.60/split.kbd
/usr/lib64/aspell-0.60/standard.kbd
/usr/lib64/aspell-0.60/tex-filter.info
/usr/lib64/aspell-0.60/tex.amf
/usr/lib64/aspell-0.60/texinfo-filter.info
/usr/lib64/aspell-0.60/texinfo.amf
/usr/lib64/aspell-0.60/url.amf

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/aspell
/V3/usr/bin/prezip-bin
/V3/usr/bin/word-list-compress
/usr/bin/aspell
/usr/bin/aspell-import
/usr/bin/precat
/usr/bin/preunzip
/usr/bin/prezip
/usr/bin/prezip-bin
/usr/bin/pspell-config
/usr/bin/run-with-aspell
/usr/bin/word-list-compress

%files dev
%defattr(-,root,root,-)
/usr/include/aspell.h
/usr/include/pspell/pspell.h
/usr/lib64/libaspell.so
/usr/lib64/libpspell.so

%files info
%defattr(0644,root,root,0755)
/usr/share/info/aspell-dev.info
/usr/share/info/aspell.info

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/aspell-0.60/context-filter.so
/V3/usr/lib64/aspell-0.60/email-filter.so
/V3/usr/lib64/aspell-0.60/markdown-filter.so
/V3/usr/lib64/aspell-0.60/nroff-filter.so
/V3/usr/lib64/aspell-0.60/sgml-filter.so
/V3/usr/lib64/aspell-0.60/tex-filter.so
/V3/usr/lib64/aspell-0.60/texinfo-filter.so
/V3/usr/lib64/libaspell.so.15.3.1
/V3/usr/lib64/libpspell.so.15.3.1
/usr/lib64/aspell-0.60/context-filter.so
/usr/lib64/aspell-0.60/email-filter.so
/usr/lib64/aspell-0.60/markdown-filter.so
/usr/lib64/aspell-0.60/nroff-filter.so
/usr/lib64/aspell-0.60/sgml-filter.so
/usr/lib64/aspell-0.60/tex-filter.so
/usr/lib64/aspell-0.60/texinfo-filter.so
/usr/lib64/libaspell.so.15
/usr/lib64/libaspell.so.15.3.1
/usr/lib64/libpspell.so.15
/usr/lib64/libpspell.so.15.3.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/aspell/bfaf730612ae1e838f897dc93179cf6960e9bb43
/usr/share/package-licenses/aspell/e60c2e780886f95df9c9ee36992b8edabec00bcc

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/aspell-import.1
/usr/share/man/man1/aspell.1
/usr/share/man/man1/prezip-bin.1
/usr/share/man/man1/pspell-config.1
/usr/share/man/man1/run-with-aspell.1
/usr/share/man/man1/word-list-compress.1

%files locales -f aspell.lang
%defattr(-,root,root,-)

