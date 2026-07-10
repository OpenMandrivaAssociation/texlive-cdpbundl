%global tl_name cdpbundl
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.36d
Release:	%{tl_revision}.1
Summary:	Business letters in the Italian style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cdpbundl
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cdpbundl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cdpbundl.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cdpbundl.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The C.D.P. Bundle can be used to typeset high-quality business letters
formatted according to Italian style conventions. It is highly
configurable, and its modular structure provides you with building
blocks of increasing level, by means of which you can compose a large
variety of letters. It is also possible to write letters divided into
sections and paragraphs, to include floating figures and tables, and to
have the relevant indexes compiled automatically. A single input file
can contain several letters, and each letter will have its own table of
contents, etc., independent from the other ones.

