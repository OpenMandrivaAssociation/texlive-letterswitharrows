%global tl_name letterswitharrows
%global tl_revision 79422

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Draw arrows over math letters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/letterswitharrows
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/letterswitharrows.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/letterswitharrows.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/letterswitharrows.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX math-mode commands for setting left and
right arrows over mathematical symbols so that the arrows dynamically
scale with the symbols. While it is possible to set arrows over longer
strings of symbols, the focus lies on single characters.

