%global packname  Rsymphony
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.1_14
Release:          1
Summary:          Symphony in R
Group:            Sciences/Mathematics
License:          EPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-14.tar.gz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    coin-or-devel
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
An R interface to the SYMPHONY MILP solver (version 5.4.3).

%prep
%setup -q -c -n %{packname}
perl -pi -e 's|^(SYMPHONY_LIBS="-lSym)"|$1 -lCgl -lOsiClp -lClp -lOsi -lCoinUtils"|;' \
    Rsymphony/configure

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
