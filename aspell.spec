#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB6D9D0CC38B327D7 (kevin@atkinson.dhs.org)
#
Name     : aspell
Version  : 0.60.6.1
Release  : 5
URL      : ftp://ftp.gnu.org/gnu/aspell/aspell-0.60.6.1.tar.gz
Source0  : ftp://ftp.gnu.org/gnu/aspell/aspell-0.60.6.1.tar.gz
Source99 : ftp://ftp.gnu.org/gnu/aspell/aspell-0.60.6.1.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.1 LGPL-2.1
Requires: aspell-bin
Requires: aspell-lib
Requires: aspell-doc
Requires: aspell-locales
Patch1: 0001-gcc7fix.patch

%description
Appendix A Installing
*********************
Aspell requires gcc 2.95 (or better) as the C++ compiler.  Other C++
compilers should work with some effort.  Other C++ compilers for mostly
POSIX compliant (Unix, Linux, BeOS, Cygwin) systems should work without
any major problems provided that the compile can handle all of the
advanced C++ features Aspell uses.  C++ compilers for non-Unix systems
might work but it will take some work.  Aspell at very least requires a
Unix-like environment (`sh', `grep', `sed', `tr', ...), and Perl in
order to build.  Aspell also uses a few POSIX functions when necessary.

%package bin
Summary: bin components for the aspell package.
Group: Binaries

%description bin
bin components for the aspell package.


%package dev
Summary: dev components for the aspell package.
Group: Development
Requires: aspell-lib
Requires: aspell-bin
Provides: aspell-devel

%description dev
dev components for the aspell package.


%package doc
Summary: doc components for the aspell package.
Group: Documentation

%description doc
doc components for the aspell package.


%package lib
Summary: lib components for the aspell package.
Group: Libraries

%description lib
lib components for the aspell package.


%package locales
Summary: locales components for the aspell package.
Group: Default

%description locales
locales components for the aspell package.


%prep
%setup -q -n aspell-0.60.6.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503344687
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1503344687
rm -rf %{buildroot}
%make_install
%find_lang aspell

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
/usr/include/*.h
/usr/include/pspell/pspell.h
/usr/lib64/libaspell.so
/usr/lib64/libpspell.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/aspell-0.60/context-filter.so
/usr/lib64/aspell-0.60/email-filter.so
/usr/lib64/aspell-0.60/nroff-filter.so
/usr/lib64/aspell-0.60/sgml-filter.so
/usr/lib64/aspell-0.60/tex-filter.so
/usr/lib64/aspell-0.60/texinfo-filter.so
/usr/lib64/libaspell.so.15
/usr/lib64/libaspell.so.15.1.5
/usr/lib64/libpspell.so.15
/usr/lib64/libpspell.so.15.1.5

%files locales -f aspell.lang
%defattr(-,root,root,-)

