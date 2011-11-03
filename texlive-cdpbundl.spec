# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/cdpbundl
# catalog-date 2007-01-31 23:04:11 +0100
# catalog-license lppl
# catalog-version 0.34
Name:		texlive-cdpbundl
Version:	0.34
Release:	1
Summary:	Business letters in the Italian style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cdpbundl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cdpbundl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cdpbundl.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cdpbundl.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The C.D.P. Bundle can be used to typeset high-quality business
letters formatted according to Italian style conventions. It is
highly configurable, and its modular structure provides you
with building blocks of increasing level, by means of which you
can compose a large variety of letters. It is also possible to
write letters divided into sections and paragraphs, to include
floating figures and tables, and to have the relevant indexes
compiled automatically. A single input file can contain several
letters, and each letter will have its own table of contents,
etc., independant from the other ones.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cdpbundl/adiseal.sty
%{_texmfdistdir}/tex/latex/cdpbundl/articoletteracdp.cls
%{_texmfdistdir}/tex/latex/cdpbundl/cdpaddon.sty
%{_texmfdistdir}/tex/latex/cdpbundl/cdpshues-example.def
%{_texmfdistdir}/tex/latex/cdpbundl/cdpshues.cfg
%{_texmfdistdir}/tex/latex/cdpbundl/epson-stylus-740.def
%{_texmfdistdir}/tex/latex/cdpbundl/hp-laserjet-4500.def
%{_texmfdistdir}/tex/latex/cdpbundl/lettcdpadi.cls
%{_texmfdistdir}/tex/latex/cdpbundl/letteracdp.cls
%doc %{_texmfdistdir}/doc/latex/cdpbundl/00readme.txt
%doc %{_texmfdistdir}/doc/latex/cdpbundl/README
%doc %{_texmfdistdir}/doc/latex/cdpbundl/manifest.txt
%doc %{_texmfdistdir}/doc/latex/cdpbundl/overview.pdf
#- source
%doc %{_texmfdistdir}/source/latex/cdpbundl/cdpbundl.dtx
%doc %{_texmfdistdir}/source/latex/cdpbundl/cdpbundl.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}