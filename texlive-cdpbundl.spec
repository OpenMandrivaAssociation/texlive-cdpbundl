Name:		texlive-cdpbundl
Version:	0.36d
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
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cdpbundl
%doc %{_texmfdistdir}/doc/latex/cdpbundl
#- source
%doc %{_texmfdistdir}/source/latex/cdpbundl

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
