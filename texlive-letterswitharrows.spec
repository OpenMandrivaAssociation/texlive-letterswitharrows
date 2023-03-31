Name:		texlive-letterswitharrows
Version:	59993
Release:	2
Summary:	Draw arrows over math letters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/letterswitharrows
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/letterswitharrows.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/letterswitharrows.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/letterswitharrows.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX math-mode commands for setting left
and right arrows over mathematical symbols so that the arrows
dynamically scale with the symbols. While it is possible to set
arrows over longer strings of symbols, the focus lies on single
characters.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/letterswitharrows
%{_texmfdistdir}/tex/latex/letterswitharrows
%doc %{_texmfdistdir}/doc/latex/letterswitharrows

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
